class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Fast pointer ko n+1 steps aage le jao
        for _ in range(n + 1):
            fast = fast.next

        # Dono pointers ko aage badhao
        while fast:
            fast = fast.next
            slow = slow.next

        # Nth node from end remove karo
        slow.next = slow.next.next

        return dummy.next