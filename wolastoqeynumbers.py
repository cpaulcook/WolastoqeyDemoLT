# Where ABRG3686 slides differed from PMP, used the slides
nums = {1:"neqt", # ABRG3686
        2:"nis",
        3:"nihi",
        4:"new",
        5:"nan",
        6:"kamahcin",
        7:"oluwikonok", 
        8:"oqomolcin",
        9:"esqonatek",
        10:"qotinsk", # ABRG3686
        11:"qotanku", # ABRG3686
        12:"nisanku",
        13:"'sanku",
        14:"newanku",
        15:"nananku",
        16:"kamahcin kehsanku",
        17:"oluwikonok kehsanku",
        18:"oqomolcin kehsanku",
        19:"esqonatek kehsanku",
        20:"nisinsk",
        30:"'sinsk",
        40:"newinsk",
        50:"naninsk",
        60:"kamahcin kehsinsk",
        70:"oluwikonok kehsinsk",
        80:"oqomolcin kehsinsk",
        90:"esqonatek kehsinsk",
        100:"qotatq", # ABRG3686
        200:"nisatq",
        300:"'satq",
        400:"newatq",
        500:"nanatq",
        600:"kamahcin kehsatq",
        700:"oluwikonok kehsatq",
        800:"oqomolcin kehsatq",
        900:"esqonatek kehsatq",
        1000:"'qotamqahk",
        2000:"nisamqahk",
        3000:"'samqahk",
        4000:"newamqahk",
        5000:"nanamqahk",
        6000:"kamahcin kehsamqahk",
        7000:"oluwikonok kehsamqahk",
        8000:"oqomolcin kehsamqahk",
        9000:"esqonatek kehsamqahk"}

# This breaks for numbers like fourteen thousand. It would probably be
# better to split numbers into chunks of 3 digits to deal with
# thousands and millions...
def to_words_helper(n, x):
    last_digit = n % 10
    result = ''
    if last_digit > 0:
        result = nums[(n % 10) * x]
    if n >= 10:
        if last_digit == 0:
            result = to_words_helper(n//10, x * 10)
        else :
            result = to_words_helper(n//10, x * 10) + " 'cel " + result
    return result

def to_words(n):
    assert 1 <= n <= 9999

    last_two_digits = n % 100
    rest = n // 100
    
    # Handle special case of 1 separately
    if n == 1:
        return 'pesq'

    if 1 <= last_two_digits <= 19:
        if rest == 0:
            return nums[last_two_digits]
        else:
            return to_words_helper(rest, 100) + " 'cel " + nums[last_two_digits]
    else:
        return to_words_helper(n, 1)


    
if __name__ == "__main__":
    import sys

    def getnumber():
        print("Enter a number (1-9999, 0 to quit)")
        return int(input())

    n = getnumber()
    while (n != 0):
        print(to_words(n))
        n = getnumber()
