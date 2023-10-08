class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

    def add_to_end(self, value):
        """
        Add a new node with the given value to the end of the linked list.

        :param value: The value to add to the end of the list.
        """
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def add_to_start(self, value):
        """
        Add a new node with the given value to the start of the linked list.

        :param value: The value to add to the start of the list.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, value):
        """
        Insert a new node with the given value after the specified node.

        :param prev_node: The node after which to insert the new node.
        :param value: The value for the new node.
        """
        if not prev_node:
            print("Previous node not found.")
            return

        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def remove_node(self, value):
        """
        Remove the first node with the given value from the linked list.

        :param value: The value of the node to remove.
        """
        if not self.head:
            print("The list is empty.")
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            print(f"Node with value {value} not found.")

    def display(self):
        """Display the elements of the linked list."""
        if not self.head:
            print("The list is empty.")
            return

        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# Example usage and demonstration
if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.add_to_end(1)
    linked_list.add_to_end(2)
    linked_list.add_to_end(3)

    print("Initial linked list:")
    linked_list.display()
    print()

    linked_list.add_to_start(0)
    print("Linked list after adding 0 to the start:")
    linked_list.display()
    print()

    linked_list.insert_after_node(linked_list.head.next, 10)
    print("Linked list after inserting 10 after the first node:")
    linked_list.display()
    print()

    linked_list.remove_node(2)
    print("Linked list after removing node with value 2:")
    linked_list.display()
    print()
