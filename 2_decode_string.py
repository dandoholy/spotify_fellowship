def decode(s):
    stack, result = [], ""

    for i in s:
        if i == "]":
            sub, num, next = "", "", None
            while next != "[":
                sub = stack.pop() + sub
                next = stack[-1]
            stack.pop()
            while stack and stack[-1] in "0123456789":
                num = stack.pop() + num
            subbed = sub * int(num)
            stack.extend(list(subbed))
        else:
            stack.append(i)

    return "".join(stack)


if __name__ == "__main__":
    print(decode("3[a]2[bc]"))
    print(decode("10[a2[c]]"))
    print(decode("2[abc]3[cd]ef"))
