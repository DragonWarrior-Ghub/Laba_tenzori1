from binarytree import Node
import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def to_binarytree(self):
        if self is None:
            return None

        node = Node(self.value)
        node.left = self.left.to_binarytree() if self.left else None
        node.right = self.right.to_binarytree() if self.right else None
        return node


def generate_tree_to_file(file, number_of_nodes):
    with open(file, 'w') as f:
        a = [i for i in range(1, number_of_nodes + 1)]
        for i in range(random.randint(1, number_of_nodes // 2)):
            a[random.randint(1, number_of_nodes - 1)] = None
        f.write(' '.join(map(str, a)))

def get_miss_input():
    miss_input = input("Введите значения для массива miss, разделяя их пробелами: ")
    miss = miss_input.split()
    miss = [int(value) for value in miss]
    return miss

def build_binary_tree_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readline().strip().split()

    # Создаем корень дерева
    root = TreeNode(int(lines[0]))

    queue = [root]
    line_index = 1

    while queue and line_index < len(lines):
        node = queue.pop(0)

        left_value = lines[line_index]
        if left_value != "None":
            left_node = TreeNode(int(left_value))
            node.left = left_node
            left_node.parent = node
            queue.append(left_node)
        line_index += 1

        if line_index >= len(lines):
            break

        right_value = lines[line_index]
        if right_value != "None":
            right_node = TreeNode(int(right_value))
            node.right = right_node
            right_node.parent = node
            queue.append(right_node)
        line_index += 1

    return root



def delete_node_and_subtree(node, miss):
    if node is None:
        return

    delete_node_and_subtree(node.left, miss)
    delete_node_and_subtree(node.right, miss)

    if node.value in miss:
        print(f"Поддеревья из узла {node.value}")
        if node.left is not None:
            print("Левое поддерево")
            print(node.left.to_binarytree())

        if node.right is not None:
            print("Правое поддерево")
            print(node.right.to_binarytree())

        # Удаление ссылок на удаляемые вершины из родительских узлов
        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None

    # Если удаленная вершина имеет значение 0, выводим все дерево
    if node.parent is None and 1 not in miss:
        print("Остальные поддеревья:")
        print(node.to_binarytree())




#Генерация файла с вершинами
if int(input('Введите 1, если нужно сгенерировать новое дерево: ')) == 1:
    generate_tree_to_file('tree.txt',
    int(input('Примерное количество вершин (n)? (будет построено дерево с количеством вершин от n//2 до n): ')))
preorder_string = "tree.txt"

#ввод с клавиатуры исключающих вершин
miss = get_miss_input()

#Создание дерева
tree = build_binary_tree_from_file(preorder_string)
print(tree.to_binarytree())


delete_node_and_subtree(tree, miss)
