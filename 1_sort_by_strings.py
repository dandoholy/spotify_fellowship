def sort_by_index(s, t):
    return "".join(sorted(s, key=lambda ch: t.index(ch)))

if __name__ == "__main__":
    print(sort_by_index("weather", "therapyw"))
    print(sort_by_index("good", "dog"))
