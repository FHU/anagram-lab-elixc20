#REMOVE PASS AND FIX THIS FUNCTION
def anagram(string1, string2):
   string1 = string1.lower()
   string2 = string2.lower()
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
    string1 = input()
    string2 = input()
    print(anagram(string1, string2))