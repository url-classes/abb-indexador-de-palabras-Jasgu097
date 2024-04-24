from node import Node_lista

class TextEditor:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history = []

    def insert_line_at_beginning(self, line_text):
        new_node = Node_lista(line_text)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.history.append(('insert', 'beginning', line_text))

    def insert_line_at_end(self, line_text):
        new_node = Node_lista(line_text)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.history.append(('insert', 'end', line_text))

    def insert_line_after(self, line_text, target_line):
        current = self.head
        while current:
            if current.data == target_line:
                new_node = Node_lista(line_text)
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                self.history.append(('insert', 'after', target_line, line_text))
                return
            current = current.next
        print("Texto no encontrado.")

    def insert_line_before(self, line_text, target_line):
        current = self.head
        while current:
            if current.data == target_line:
                new_node = Node_lista(line_text)
                new_node.prev = current.prev
                new_node.next = current
                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node
                current.prev = new_node
                self.history.append(('insert', 'before', target_line, line_text))
                return
            current = current.next
        print("Texto no encontrado.")

    def delete_line(self, line_number):
        current = self.head
        index = 0
        while current:
            if index == line_number:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.history.append(('delete', line_number, current.data))
                return
            current = current.next
            index += 1
        print("Linea de numero no encontrada.")

    def display_text(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def search_text(self, keyword):
        current = self.head
        while current:
            if keyword in current.data:
                print(current.data)
            current = current.next

    def replace_text(self, old_text, new_text):
        current = self.head
        while current:
            if old_text in current.data:
                current.data = current.data.replace(old_text, new_text)
            current = current.next

    def undo(self):
        if self.history:
            action = self.history.pop()
            if action[0] == 'insert':
                if action[1] == 'beginning':
                    self.delete_line(0)
                elif action[1] == 'end':
                    self.delete_line(-1)
                elif action[1] == 'after':
                    self.delete_line(self.find_line_index(action[2]) + 1)
                elif action[1] == 'before':
                    self.delete_line(self.find_line_index(action[2]) - 1)
            elif action[0] == 'delete':
                if action[1] == 0:
                    self.insert_line_at_beginning(action[2])
                else:
                    self.insert_line_after(action[2], self.find_line(action[1] - 1))
            return True
        else:
            print("No acciones para el undo.")
            return False

    def redo(self):
        print("Redo no implementado aun")
        # Add redo functionality here

    def save_file(self,file_path):
        with open(file_path,"w") as file:
            current = self.head
            while current:
                file.write(current.data + "\n")
                current = current.next

    def load_file(self,file_path):
        self.head=None
        self.tail=None

        with open(file_path,"r") as file:
            lines= file.readlines()
            for line in lines:
                self.insert_line_at_end(line.strip())

    def find_line(self, line_number):
        current = self.head
        index = 0
        while current:
            if index == line_number:
                return current.data
            current = current.next
            index += 1
        return None

    def find_line_index(self, line_text):
        current = self.head
        index = 0
        while current:
            if current.data == line_text:
                return index
            current = current.next
            index += 1
        return -1

    def recursividad(self):
        pass



