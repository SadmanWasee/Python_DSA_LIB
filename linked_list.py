class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None
    

    
    def append(self, data):

        #Creating a new node
        new_node = Node(data)

        #Checking if the head node / first node exists
        if not self.head:
            self.head = new_node
            return
        
        #Initializing the last node as the head node / first node
        last_node = self.head

        #While there exisits next node to the last node
        while last_node.next:
            last_node = last_node.next #Resign the last node as the next node
        
        #Finally the next node to last node will be the new node
        last_node.next = new_node

    def prepend(self, data):

        # Creating a new node
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        
    def print_list(self):

        current_node = self.head

        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next
        print("None")

    def insert_after(self, prev_node, data):

        # Checking if the list is empty
        if not self.head:
            print("The list is empty")

        # Assigning the current node as first node
        current_node = self.head

        #Creating a new node
        new_node = Node(data)

        #Continue looping while there exists a node next to the current node
        while current_node:
            
            # If the data does not exist in the list print and return
            if current_node.data == "None":
                print("The previous node does not exist")
                return
            
            # If it finds the data in the current node
            elif current_node.data == prev_node:

                # Store the next in a temp variable 
                temp_node = current_node.next
                # Point the current node to the new node 
                current_node.next = new_node
                # Point the new node to the temp node
                new_node.next = temp_node

                return
            # Update the current node 
            current_node = current_node.next
        print("Successfully updated the value")

    def del_by_val(self, data):

        # Starting with the first node as the current node
        current_node = self.head

        # If the current / first node is equal to the data passed by the user
        if current_node and current_node.data == data:
            # We will unlink the current node and assigh the next node as the first node
            self.head = current_node.next
            # Unlink current node 
            current_node = None
            return
        
        # Previous node 
        prev_node = None

        # While the current node and the data is not equal to the data loop through the list 
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        # If we reach the end of the list without finding the given data return 
        if not current_node:
            return
        
        # At this stage the current node should contain the data passed by the user as we exited the while loop
        # So we will join the previous node to the next node to the current node
        prev_node.next = current_node.next
        # And unassign the current node. 
        current_node = None
    
    def del_by_pos(self, pos):

        # If the list is empty or the user entered a negative value for index we will exit the function
        if not self.head or pos<0:
            return
        
        count = 0

        # Starting with the first node 
        current_node = self.head

        # If the position is 0 we will unlink the first node 
        if pos == 0 :
            self.head = current_node.next
            current_node = None
            return
        
        # To keep the track of the previous node
        previous_node = None

        # While current node exisits 
        while current_node:

        # If count equal to position break else keep looping through the list    
            if count == pos:
                break

            count+=1
            previous_node = current_node
            current_node = current_node.next

        # If the position is out of bounds return 
        if not current_node:
            return
        
        # At this point we must have reached the position
        # The next node to the previous node is the next node to the current node
        previous_node.next = current_node.next
        current_node = None

    def update(self, pos, data):

        # If the list is empty or the position is less than 0 return 

        if not self.head or pos < 0:
            return 
        
        # Initilaization 
        count = 0 

        current_node = self.head

        # If the position is 0 then we will update the data of the first node 
        if pos == 0 : 

            current_node.data = data
            return 
        
        # Loop throught the list until we reach the position
        while current_node : 

            if count == pos:
                break

            current_node = current_node.next
            count += 1

        # If the position is out of bounds return 
        if not current_node:
            return
        
        # At this point we have reached the position 
        # Update the value of the current node 
        current_node.data = data

            