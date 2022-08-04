class Stack():
    def __init__(self, some_list):
        if type(some_list) == list:
            self.some_list = some_list
            print(f"Stack {some_list}")
        else:
            self.some_list = [some_list]
            print(f"Stack {[some_list]}")
    def isEmpty(self):
        if len(self.some_list) == 0:
            return True
        else:
            return False
    def push(self,new_el):
        self.some_list.append(0)
        for i in reversed(range(len(self.some_list)-1)):
            self.some_list[i+1] = self.some_list[i]
        self.some_list[0] = new_el
    def pop(self):
        x = self.some_list[0]
        self.some_list = self.some_list[1:]
        return x
    def peek(self):
        return self.some_list[0]
    def size(self):
        return len(self.some_list)

                #Я не сразу понял зачем нужен именно стэк для задачи и пытался найти решение арифметически
def skobki(s):  #Круто если вы знаете, чем дополнить мою функцию, чтобы она заработала
    kv = 0      #Неверный ответ выдает из-за 17 символа ']' строки '[([])((([[[]]])))]{()}'
    kr = 0
    fig = 0
    pred = 0
    for i in range(len(s)):
        if kv < 0 or kr < 0 or fig < 0:
            return False
        if s[i] == '[':
            kv += 1
            pred = i
        elif s[i] == '(':
            kr += 1
            pred = i
        elif s[i] == '{':
            fig += 1
            pred = i
        elif s[i] == ']' and s[pred] == '[':
            kv -= 1
            if pred > 0:
                pred -= 1
        elif s[i] == ')' and s[pred] == '(':
            kr -= 1
            if pred > 0:
                pred -= 1
        elif s[i] == '}' and s[pred] == '{':
            fig -= 1
            if pred > 0:
                pred -= 1
        else:
            return False
    if kv == 0 and kr == 0 and fig == 0:
        return True
    else:
        return False

def skobki_stack(s):    #Но столкнувшись с неразешимой(для себя) проблемой, понял при чем тут стэк
    open_s = ['(', '[', '{']
    res = Stack([])
    for sim in s:
        if sim in open_s:
            res.push(sim)
        elif res.size() > 0:
            if sim == ']' and res.peek() == '[':
                res.pop()
            elif sim == '}' and res.peek() == '{':
                res.pop()
            elif sim == ')' and res.peek() == '(':
                res.pop()
            else:
                return False
        else:
            return False
    if res.size() == 0:
        return True
    else:
        return False



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')
    y = Stack(4)
    print(y.isEmpty())
    y.push(5)
    y.push(14)
    y.push([])
    print(y.peek())
    print(y.size())
    print(skobki_stack('(((([{}]))))'))
    print(skobki_stack('[([])((([[[]]])))]{()}'))
    print(skobki_stack('{{[()]}}'))
    print(skobki_stack('}{}'))
    print(skobki_stack('{{[(])]}}'))
    print(skobki_stack('[[{())}]'))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
