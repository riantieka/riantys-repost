# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_after(self, prev_node_data, new_data):
        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node dengan data '{prev_node_data}' tidak ditemukan.")

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Membuat Playlist
playlist = LinkedList()
playlist.append("Intro Musik")
playlist.append("Lagu Night Changes")
playlist.append("Lagu Double Take")

print("Playlist sebelum disisipkan:")
playlist.print_list()

# Menyisipkan Lagu Iklan setelah Intro Musik
playlist.insert_after("Intro Musik", "Lagu Iklan")

print("\nPlaylist setelah disisipkan:")
playlist.print_list()

