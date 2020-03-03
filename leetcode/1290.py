# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

def getDecimalValue(self, head: ListNode) -> int:
    value = ''
    while head:
        value += str(head.val)
        head = head.next
    return(int(value,2))