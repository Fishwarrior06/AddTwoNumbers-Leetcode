from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            valor1 = l1.val if l1 else 0
            valor2 = l2.val if l2 else 0

            suma = valor1 + valor2 + carry
            carry = suma // 10
            nuevo_digito = suma % 10

            current.next = ListNode(nuevo_digito)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

# Ejemplo de uso:
# Crear los números 342 y 465
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
# Imprimir el resultado (807)
while result:
    print(result.val)  # Debería imprimir 7, luego 0, luego 8
    result = result.next