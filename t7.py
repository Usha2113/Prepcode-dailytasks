# Count Vowels and Consonants
def count_vowels_and_consonants(s):
   
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    # return after the loop (was incorrectly indented inside the loop)
    return v_count, c_count


if __name__ == "__main__":
    s = input("Enter a string: ")
    v_count, c_count = count_vowels_and_consonants(s)
    print("vowels:", v_count, "consonants:", c_count)

