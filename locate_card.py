# Write a program to find the position of a given number in a list of numbers arranged in descending order. We also
# need to minimize the number of times we access elements from the list.

def locate_card(cards, query):
    left, right = 0, len(cards) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            right = mid - 1
        else:
            left = mid + 1
    return -1

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 10

cardResult = print(locate_card(cards, query))  # Output: 2

# Testing for the test case
test = {
    "cards": [13, 11, 10, 7, 4, 3, 1, 0],
    "query": 10
}


testResult = print(locate_card(test["cards"], test["query"]))  # Output: 2

finalResult = testResult == cardResult

print(finalResult)