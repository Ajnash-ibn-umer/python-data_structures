import stack as st

stack=st.Stack()


def is_match(ch1,ch2):
    match_dic={
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dic[ch1]==ch2

def balance(str):

    for ch in str:

        if ch == '{' or ch=='[' or ch=='(':
            stack.push(ch)
        if ch == '}' or ch==']' or ch==')':
            if stack.length()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.length()==0



if __name__=='__main__':
    print(balance('({a+b})'))
