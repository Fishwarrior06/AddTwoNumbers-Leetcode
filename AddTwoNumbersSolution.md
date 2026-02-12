Here's the solution to the Add Two Numbers problem from Leetcode.

## CASE
In this question we are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reversed order** and each of their nodes contains a single digit. Add the two numbers and then return the sum as a linked list.

**Constrains**
- The number of nodes in each linked list is in the range ```[1, 100]```.
- ```0 <= Node.val <= 9```.
- It is guaranteed that the list represents a number that does not have leading zeros.

## SOLUTION
The solution to this case is the next one.

First we have to define our class ```LinkedNode```  with its method that initiates at value 0 and defines ```self.val``` as **val** and ```self.next``` as **next**.

Then we define our class Solution and its method
In this case we define the method that is as following```addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode] and the result should be another Optional[ListNode])```.

Following this we can explain that
- self is basically itself.
- l1 is optional. (meaning that values can be optional in as in that it can have values or not)
- Same with l2.
- The case requires us to create a new linkedlist after with the two numbers inside the linkedlist added.

Then we define its atributes
```Dummy```: is definded as value 0, dummy is always called whenever theres a carry
```current = dummy```: used with carry when there maybe more numbers in one linkedlist than in the other.
```carry = 0```: we define carry as 0 and when we get two-digit numbers the carry takes the first number (```unit```) and we write to the linkedlist the second number (```dozen```).

Then we have out ```while```, ```if-else``` cases

So the basic way to sum this up. ```While l1 or l2 or carry```.
Has valor1 and valor2 that equal to l1 and l2 respectively
We use the ```val``` function that we created earlier on the linkedlist. 
If l1 else 0, same with l2.

Then we proceed to ```suma``` which adds, value 1 with value 2 and if the number is over 9 it will save it on carry and use it in the next case
**For example**
l1 = [2,4,3], l2 = [5,6,4]and we are looking for an output of l = [7,0,8].

so in this case the as stated by the case the numbers in the linkedlist are saved in reverse. So when translating it to make the sum we would need to put them in this way

342 + 465 = 807

In this case the easiest way to understand **THIS** case would be the following:
If the numbers are saved in reverse we need to see them as a normal sum. So the *standard* way to make sum would be by first adding up the units, then adding the dozens and then by adding the hundreds.
We take the first linkedlist saved numbers: ```[2,4,3].
So taking the example I mentioned previously we can infere that 2 is the unit, 4 is the dozen and 3 is the hundred. 
We make them their normal number ```342```.

So by doing this we can continue the code by explaining how we just sum the first 2 numbers and then goes to the next and so on until we have no more numbers in the linkedlist and we have also used all the carried numbers.

## ANSWER
So now we print the solution.
l1 = [2,4,3], l2 = [5,6,4]
So we make the sum which is ```l1 + l2 + carry```
2 + 5 + 0 = 7 (No carry in this case)
4 + 6 + 0 = 10 but it writes 0 due to being a two-digit number and we have carry so we jut carry 1.
3 + 4 + 1 = 8
Now we have no ```carry``` numbers to add up and no more numbers in the linkedlist.

So we end up by having 807.
And its saved on the linkedlist like this ```[7, 0, 8]
7 units, 0 dozens, 8 hundrends = 807
