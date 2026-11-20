# Name: Max Aikins
# COMP 250 - Project 3


from collections import deque


class Node:
    def __init__(self,id, name, major):
        self.id = id
        self.name = name
        self.major = major
        self.left = None
        self.right = None

class BinarySearchTree:


    def __init__(self):
        self.source = None

    def inOrder(self,node):

        if node == None:
            return

        
        self.inOrder(node.left)

        print(node.id, node.name)

        self.inOrder(node.right)



    def preOrder(self,node):

        if node == None:
            return

        print(node.id, node.name)  
        
        self.preOrder(node.left)

        self.preOrder(node.right)


    def postOrder(self,node):
    
        if node == None:
            return

        self.postOrder(node.left)

        self.postOrder(node.right)

        print(node.id, node.name)

    def count(self,node):

        if node == None:
            return 0

        # recursive call
        # returns 1 + the count of the left + the count of the right
        # both of these expressions will simplify down to a string of 1's being added together corresponding to how many nodes each side visited. each 1 represents a node
        return 1 + self.count(node.left) + self.count(node.right)


    def height(self,node):

        if node == None:
            return 0


        # calculate the height of each side of the tree
        left_height = self.height(node.left)

        right_height = self.height(node.right)

        # compare the two heights since one side of the tree can be deeper than the other and return the biggest height
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1






    def insert(self,node):

        # keep track of current node
        cur_node = self.source

        # if the tree was empty, make the node that we are inserting the root
        if self.source == None:
            self.source = node
            return True

        # loop infinitely - we want to do this set of checks until we hit one of the return statements inside
        # if the id is less than the id of the current node we are on, move to its lesser child
        # we do this check all the way down until we get to a node where the child on the side we need to go to is None
        # then in the spot that we arrived at that is currently None we put the new Node

        # we also check if the current nodes id is equal to the id of the node that we are inserting, in which case we return false and print a message

        while(True):
            if node.id < cur_node.id:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = node
                    return True

            elif node.id > cur_node.id:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = node
                    return True
            else:
                print("Cannot Attach Duplicate ID")
                return False



    def search(self, student_id):
        # keep track of the path we took to get to the node we are searching for
        # we will just append every node that we look at to this path list 
        path = []

        # check if the tree is empty, if so return none because we cant search for anything in a tree that doesnt exist
        if self.source == None:
            print("The Tree is Empty")
            # still return none and path even though there is nothing in path so we dont break anything around the method call that might be assuming it will get 2 variables
            return None, path


        cur_node = self.source

    
        while(True):
            # append current node to the path
            path.append(cur_node)

            # if the id we are looking for is less than the id of the current node we are looking at, then we need to look to the left
            # we do this because the way the tree is structured the lesser values will always be to the left
            # since all lesser values compared to where we currently are will be to our left, every time we see that our value is less than the value we are on we go left
            # we do the same thing for the right, if the id we are looking for is bigger than the id of the current node, we know the node we are looking for will be to the right of the current node.
            if student_id < cur_node.id:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    # if we get to a node that is None on either side we know we have looked through all of the nodes that could 
                    # have possible contained the value we are looking for so we return None
                    return None, path

            elif student_id > cur_node.id:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    return None, path
            else:
                # if we know the id of the current node is not greater than or less than the value we are looking for, the current node must contain it
                return cur_node, path

# create the tree object 
tree = BinarySearchTree()

# makes sure the user input is an int and asks repeatedly until it gets one
def get_valid_id(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Student ID must be an integer.")

# makes sure the users menu choice will not throw any errors
def get_menu_choice():
    while True:
        choice = input("Select from the menu (1-7): ").strip()
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            return int(choice)
        print("Invalid selection. Please enter a number from 1 to 7.")

# helper function to check if the tree is empty since it is a global varible
def tree_is_empty():
    if tree.source == None:
        print("The tree is empty. Add a student first.")
        return True
    return False

# gets the input necessary for the Node object, creates it, and then passes it to the insert method on the BinarySearchTree class
def add_student():
    student_id = get_valid_id("Enter student ID: ")
    name = input("Enter student name: ").strip()
    major = input("Enter student major: ").strip()

    student = Node(student_id, name, major)
    if tree.insert(student):
        print(f"Student {name} (ID {student_id}) added.")


# gets user unput for the student id and calls the search() method on the BinarySearchTree class
def search_student():
    if tree_is_empty():
        return
    student_id = get_valid_id("Enter the student ID to search for: ")

    found, path = tree.search(student_id)

    if found:
        print(f"Found: ID {found.id}, Name: {found.name}, Major: {found.major}")
    else:
        print(f"Student with ID {student_id} not found.")

    # loop through all of the nodes in the path list and populate a new list called ids with all of their id's
    ids = []
    for node in path:
        ids.append(str(node.id))

    # join method returns a string of the list of id's and puts the string you call it on in between each id in the list
    # found this method on W3Schools , https://www.w3schools.com/python/ref_string_join.asp
    print("Path: " + " -> ".join(ids))
    print(f"Nodes checked: {len(path)}")


def dfs():
    # check if the tree is empty since we wouldnt search through an empty tree
    if tree_is_empty():
        return

    print("\nChoose a DFS traversal:")
    print("  1: Pre-order")
    print("  2: In-order")
    print("  3: Post-order")
    # sanitize input to make sure the input choice is valid
    while True:
        choice = input("Choose an option from the list (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            break
        print("Invalid choice. Please enter 1, 2, or 3.")

    # call corresponding method on the BinaryTreeClass passing in the source
    # we pass in the source here because then we can easily make that method recursive itself instead of having to call another recursive method
    # this is because the recursive method needs to have the current node as a paremeter so it can continue calling itself with different nodes
    if choice == "1":
        tree.preOrder(tree.source)
    elif choice == "2":
        tree.inOrder(tree.source)
    else:
        tree.postOrder(tree.source)


def bfs():
    if tree_is_empty():
        return

    # create the queue and append the source 
    # keep track of the level which will be incremented every time through the while loop
    queue = deque()
    queue.append(tree.source)
    level_num = 1

    # keep track of all of the nodes in the current level
    # pop them off one at a time and append their children to populate the queue with the next level of nodes
    # once the queue is empty we know we have gotten through all of the nodes in the tree
    while(queue):
        level_size = len(queue)
        level = []

        # just need to loop through as many times as there are items in the level
        # we need this for loop to display the levels one at a time
        # the way we did it in class, the queue was constantly revolving and there was no differentiation between level it just popped the next node and appended the nodes children
        # with the loop, every iteration through the while loop is 1 level of the tree so we can keep track of each level and print them out
        for i in range(level_size):
            cur_node = queue.popleft()
            level.append(str(cur_node.id))

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

        print(f"Level {level_num}: " + ", ".join(level))
        level_num += 1


def stats():
    if tree_is_empty():
        return
    # call the height and count methods on the tree object which is an object of the BinarySearchTree class
    total = tree.count(tree.source)
    height = tree.height(tree.source)

    print(f"Total students: {total}")
    print(f"Tree height: {height}")


def min_max():
    if tree_is_empty():
        return

    # go down the tree by looking at the left most node every time, once you reach a node where there is nothing to the left of it, you know you have found the smallest value
    cur_node = tree.source
    while(cur_node.left):
        cur_node = cur_node.left
    print(f"Smallest ID: {cur_node.id}, Name: {cur_node.name}, Major: {cur_node.major}")

    # same thing but on the right side for the largest value
    cur_node = tree.source
    while(cur_node.right):
        cur_node = cur_node.right
    print(f"Largest ID: {cur_node.id}, Name: {cur_node.name}, Major: {cur_node.major}")


loop = True
# main loop so you can do multiple actions in the same run
while(loop):
    print("\n===== Student BST Menu =====")
    print("1. Add a new student")
    print("2. Search for a student by ID")
    print("3. Display all students (DFS: pre-order, in-order, or post-order)")
    print("4. Display all students (BFS, level by level)")
    print("5. Display tree stats (total students and tree height)")
    print("6. Display students with the smallest and largest IDs")
    print("7. Exit")
    print("=============================")

    selection = get_menu_choice()

    if selection == 1:
        add_student()
    elif selection == 2:
        search_student()
    elif selection == 3:
        dfs()
    elif selection == 4:
        bfs()
    elif selection == 5:
        stats()
    elif selection == 6:
        min_max()
    elif selection == 7:
        print("Goodbye!")
        loop = False


"""
Time Complexity Questions

1. O(log n):
When the IDs were added as 50, 30, 70, 20, 40, 60, 80, the tree was balanced, and
searching for 80 checked 3 nodes (50 -> 70 -> 80). When the IDs were added sequentially from 10 to 70 counting by 10's every new node went to the right, so the tree became a straight
line. Searching for 70 checked all 7 nodes. Every comparison in BST moves down one level,
so the number of nodes checked depends on the height of the tree. A balanced tree has a
height of about log n because each level doubles the number of nodes, so each step cuts
 the remaining number of nodes left to search in half and the search is O(log n). An unbalanced tree can have a height of n,
so the search becomes O(n), we saw this with the example where we added 10,20...,70.

2. O(n log n):
Building the tree means inserting n students one at a time. Each insert into a balanced
tree takes about log n steps, so n inserts take about n * log n steps, which is
O(n log n). For 1,000 students, log base 2 of 1000 is about 10, so building the tree takes
about 1,000 * 10 = 10,000 steps.
"""
