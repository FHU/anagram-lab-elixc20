#REMOVE PASS AND FIX THIS FUNCTION
def anagram(string1, string2):
   if string1.isspace() == True or string2.isspace() == True:
        return False
   string1 = string1.lower()
   string2 = string2.lower()
   string1 = string1.split()
   string2 = string2.split()
   string1 = ''.join(string1)
   string2 = ''.join(string2)
   if (len(string1) == len(string2)):
    new_string1 = sorted(string1)
    new_string2 = sorted(string2)
    if (new_string1 == new_string2):
        return ('True')
    else:
        return ('False')
   else:
      return ('False')

if __name__ == '__main__':
    word1 = input()
    word2 = input()
    print(anagram(word1, word2))