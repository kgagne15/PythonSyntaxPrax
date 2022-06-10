def print_upper_words(words, must_start_with = 'e'):
    """ For list of words each word will print on separate lines and 
    in uppercase

        >>> print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
        HELLO
        HEY
        YO
        YES

        >>> print_upper_words(['ego', 'excellent', 'envy', 'mean', 'merry'])
        EGO
        EXCELLENT
        ENVY

        >>> print_upper_words(['nautilus', 'prejudice', 'wired', 'egalitarian'])
        EGALITARIAN

    
    """
    for word in words: 
        for letter in must_start_with:
            if word[0].lower() == letter:
                print(word.upper())
        
        


print_upper_words(['nautilus', 'prejudice', 'wired', 'egalitarian'])
print_upper_words(['ego', 'excellent', 'envy', 'mean', 'merry'])
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
print_upper_words(["Programming", "is", "pretty", "fun"])