
def reverse_list(l):
    """rev=[]
    print("list has {0} elements".format(len(l)))
    for i in range(1,len(l)+1):
        print(l[-i])
        rev.append(l[-i])
    """
    """
    Reverses order of elements in list l.
    """
    #return rev
    return l[::-1]


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

""" debugging reverse
test_reverse_list
list=[1,2,3]
rev=reverse_list(list)
print(rev)
"""

# ------------------------------------------------------------------------------

def reverse_string(s):
    """
    Reverses order of characters in string s.
    """
    return s[::-1]


def test_reverse_string():
    assert reverse_string("foobar") == "raboof"

#print(reverse_string("Kasia"))

# ------------------------------------------------------------------------------

def is_english_vowel(c):
    vowels=['a','e','i','o','u','y']
    #print ("I got {0} and lower case is {1}".format(c,c.lower()))
    if c.lower() in vowels:
        #print ("VOWEL")
        return True
    else:
        #print("NOT A VOWEL")
        return False
    """
    Returns True if c is an english vowel
    and False otherwise.
    """

#is_english_vowel("K")


def test_is_english_vowel():
    assert is_english_vowel('a')
    assert is_english_vowel('e')
    assert is_english_vowel('i')
    assert is_english_vowel('o')
    assert is_english_vowel('u')
    assert is_english_vowel('y')
    assert is_english_vowel('A')
    assert is_english_vowel('E')
    assert is_english_vowel('I')
    assert is_english_vowel('O')
    assert is_english_vowel('U')
    assert is_english_vowel('Y')
    assert not is_english_vowel('k')
    assert not is_english_vowel('z')
    assert not is_english_vowel('?')


# ------------------------------------------------------------------------------

def count_num_vowels(s):
    count=0
    for i in range (0,len(s)):
        #print("{0}".format(s[i]))
        if is_english_vowel(s[i]):
            count = count+1
    """
    Returns the number of vowels in a string s.
    """
    #print("There are {0} vowels in {1}".format(count,s))
    return count

#count_num_vowels("Kasia")


def test_count_num_vowels():
    sentence = "hey ho let's go"
    assert count_num_vowels(sentence) == 5
    sentence = "HEY ho let's GO"
    assert count_num_vowels(sentence) == 5
    paragraph = """She told me her name was Billie Jean,
                   as she caused a scene
                   Then every head turned with eyes
                   that dreamed of being the one
                   Who will dance on the floor in the round"""
    assert count_num_vowels(paragraph) == 54


# ------------------------------------------------------------------------------

def string_histogram(l):
    hist=""
    for i in range(0,len(l)):
        hist=hist+"#"
    hist=hist+"\n"
    """
    Converts a list of integers into a simple string histogram.
    """
    #print("String histogram for {0}\n{1}".format(l,hist))
    return hist

#histogram("Kasia")

def histogram(l):
    hist=""
    print("Number of elements is {0}".format(len(l)))
    for pos in range(0,len(l)):
        number=l[pos]
        print("Position {0} number {1}".format(pos, number))
        for i in range(0,number):
            hist=hist+"#"
        if pos < len(l)-1:
            hist=hist+"\n"
        print("Round for {0} gives:\n{1}".format(number,hist))
    """
    Converts a list of integers into a simple string histogram.
    """
    return hist

#histogram([1,3,5])
#histogram([2,5,1])

def test_histogram():
    assert histogram([2, 5, 1]) == '##\n#####\n#'


# ------------------------------------------------------------------------------

def get_word_lengths(s):
    word_lengths=[]
    all_words=s.split(" ")
    for word in all_words:
        word_lengths.append(len(word))
        print("Adding {0} for {1}".format(len(word),word))
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    return word_lengths

#get_word_lengths("Kasia is getting really hungry...")

def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]

# ------------------------------------------------------------------------------

def find_longest_word_easy(s):
    longest=""
    max_length=0
    all_words=s.split(" ")
    for word in all_words:
        #print("Current word {0} length {1}".format(word,len(word)))
        if len(word) > max_length:
            longest=word
            max_length=len(word)
            #print("best!")
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    #print("Longest word {0} length {1}".format(longest,max_length))
    return longest

def find_longest_word(s):
    all_words_lengths=get_word_lengths(s)
    max_pos=all_words_lengths.index(max(all_words_lengths))
    words=s.split(" ")
    longest_word=words[max_pos]
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    #print("Longest word {0} length {1}".format(longest,max_length))
    return longest_word

#find_longest_word("Three tomatoes are walking down the street")
#find_longest_word("foo foo1 foo2 foo3")

def test_find_longest_word():
    text = "Three tomatoes are walking down the street"
    assert find_longest_word(text) == "tomatoes"
    text = "foo foo1 foo2 foo3"
    assert find_longest_word(text) == "foo1"


# ------------------------------------------------------------------------------

def validate_dna(s):
    # THIS SHOULD REALLY INCLUDE n to be useful!!!
    dna=['a','c','t','g']
    for pos in range(0,len(s)):
        if s[pos].lower() not in dna:
            print("This is not proper DNA {0}".format(s[pos]))
            return False
    """
    Return True if the DNA string only contains characters
    a, c, t, or g (lower or uppercase). False otherwise.
    """
    return True


def test_validate_dna():
    assert validate_dna('CCGGAAGAGCTTACTTAGccggaagagcttacttag')
    assert not validate_dna('xCCGGAAGAGCTTACTTAGccggaagagcttacttag')


# ------------------------------------------------------------------------------

def base_pair(c):
    c_lower=c.lower()
    if c_lower == "a":
        return "t"
    elif c_lower == "t":
        return "a"
    elif c_lower == "g":
        return "c"
    elif c_lower == "c":
        return "g"
    else:
        return "unknown"
    """
    Return the corresponding character (lowercase)
    of the base pair. If the base is not recognized,
    return 'unknown'.
    """


def test_base_pair():
    assert base_pair('a') == 't'
    assert base_pair('t') == 'a'
    assert base_pair('c') == 'g'
    assert base_pair('g') == 'c'
    assert base_pair('A') == 't'
    assert base_pair('T') == 'a'
    assert base_pair('C') == 'g'
    assert base_pair('G') == 'c'
    assert base_pair('x') == 'unknown'
    assert base_pair('foo') == 'unknown'


# ------------------------------------------------------------------------------

def transcribe_dna_to_rna(s):
    rna=""
    for pos in range(0,len(s)):
        if s[pos].upper() == "T":
            rna=rna+"U"
        else:
            rna=rna+s[pos].upper()
    """
    Return string s with each letter T replaced by U.
    Result is always uppercase.
    """
    return rna


def test_transcribe_dna_to_rna():
    dna = 'CCGGAAGAGCTTACTTAGccggaagagcttacttag'
    assert transcribe_dna_to_rna(dna) == 'CCGGAAGAGCUUACUUAGCCGGAAGAGCUUACUUAG'


# ------------------------------------------------------------------------------

def get_complement(s):
    complement=""
    for pos in range(0,len(s)):
        complement=complement+base_pair(s[pos]).upper()
    return complement
    """
    Return the DNA complement in uppercase
    (A -> T, T-> A, C -> G, G-> C).
    """


def test_get_complement():
    assert get_complement('CCGGAAGAGCTTACTTAG') == 'GGCCTTCTCGAATGAATC'
    assert get_complement('ccggaagagcttacttag') == 'GGCCTTCTCGAATGAATC'


# ------------------------------------------------------------------------------

def get_reverse_complement(s):

    """
    Return the reverse complement of string s
    (complement reversed in order).
    """
    return get_complement(reverse_string(s))


def test_get_reverse_complement():
    assert get_reverse_complement('CCGGAAGAGCTTACTTAG') == 'CTAAGTAAGCTCTTCCGG'
    assert get_reverse_complement('ccggaagagcttacttag') == 'CTAAGTAAGCTCTTCCGG'


# ------------------------------------------------------------------------------

def remove_substring(substring, string):
    new_str = string.replace(substring,'')
    """
    Returns string with all occurrences of substring removed.
    """
    return new_str


def test_remove_substring():
    assert remove_substring('GAA', 'CCGGAAGAGCTTACTTAG') == 'CCGGAGCTTACTTAG'
    assert remove_substring('CCG', 'CCGGAAGAGCTTACTTAG') == 'GAAGAGCTTACTTAG'
    assert remove_substring('TAG', 'CCGGAAGAGCTTACTTAG') == 'CCGGAAGAGCTTACT'
    assert remove_substring('GAA', 'GAAGAAGAA') == ''


# ------------------------------------------------------------------------------

def get_position_indices(triplet, dna):
    
    """
    Returns list of position indices for a specific triplet (3-mer)
    in a DNA sequence. We start counting from 0
    and jump by 3 characters from one position to the next.
    """
    return None


def test_get_position_indices():
    assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAG') == [1]
    assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAGGAAGAA') == [1, 6, 7]


# ------------------------------------------------------------------------------

def get_3mer_usage_chart(s):
    """
    This routine implements a 'sliding window'
    and extracts all possible consecutive 3-mers.
    It counts how often they appear and returns
    a list of tuples with (name, occurrence).
    The list is alphabetically sorted by the name
    of the 3-mer.
    """
    return None


def test_get_3mer_usage_chart():
    s = 'CCGGAAGAGCTTACTTAGGAAGAA'
    result = []
    result.append(('AAG', 2))
    result.append(('ACT', 1))
    result.append(('AGA', 2))
    result.append(('AGC', 1))
    result.append(('AGG', 1))
    result.append(('CCG', 1))
    result.append(('CGG', 1))
    result.append(('CTT', 2))
    result.append(('GAA', 3))
    result.append(('GAG', 1))
    result.append(('GCT', 1))
    result.append(('GGA', 2))
    result.append(('TAC', 1))
    result.append(('TAG', 1))
    result.append(('TTA', 2))
    assert get_3mer_usage_chart(s) == result


# ------------------------------------------------------------------------------

def read_column(file_name, column_number):
    """
    Reads column column_number from file file_name
    and returns the values as floats in a list.
    """
    return None


def test_read_column():

    import tempfile
    import os

    text = """
1   0.1  0.001
2   0.2  0.002
3   0.3  0.003
4   0.4  0.004
5   0.5  0.005
6   0.6  0.006"""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write(text)

    # and now we pass the file name to the function which will read the column
    assert read_column(file_name, 2) == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------

def character_statistics(file_name):
    """
    Reads text from file file_name, then
    lowercases the text, and then returns
    a tuple (x, y), where x is the most abundant
    and y is the least abundant character found.
    Use the isalpha() method to figure out
    whether the character is in the alphabet.
    """
    return None


def test_character_statistics():

    import tempfile
    import os

    text = """
To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When we have shuffled off this mortal coil,
Must give us pause: there's the respect
That makes calamity of so long life;
For who would bear the whips and scorns of time,
The oppressor's wrong, the proud man's contumely,
The pangs of despised love, the law's delay,
The insolence of office and the spurns
That patient merit of the unworthy takes,
When he himself might his quietus make
With a bare bodkin? who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscover'd country from whose bourn
No traveller returns, puzzles the will
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience does make cowards of us all;
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry,
And lose the name of action.--Soft you now!
The fair Ophelia! Nymph, in thy orisons
Be all my sins remember'd."""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write(text)

    # and now we pass the file name to the function which will get the stats
    (most_abundant, least_abundant) = character_statistics(file_name)
    assert (most_abundant, least_abundant) == ('e', 'q')

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------

def pythagorean_triples(n):
    """
    Returns list of all unique pythagorean triples
    (a, b, c) where a < b < c <= n.
    """
    l = []
    # loop over all a < b < c <= n
    for c in range(1, n + 1):
        for b in range(1, c):
            for a in range(1, b):
                if a*a + b*b == c*c:
                    l.append((a, b, c))
    return l


# ------------------------------------------------------------------------------

def test_pythagorean_triples():
    pass  # so far we do not test anything, check also test coverage
