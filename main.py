#REMOVE PASS AND FIX THIS FUNCTION
def anagram(string1, string2):
    list1 = list(string1)
    list1.sort()
    list2 = list(string2)
    list2.sort()

    if list1 == list2:
        return ('True')
    if list1 != list2:
        return ('False')

if __name__ == '__main__':
    input1 = str(input())
    input2 = str(input())

    list1 = []
    list2 = []

    print(anagram(list1, list2))