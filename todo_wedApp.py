import streamlit as st
from function import write_todos, get_todos

all_todos = get_todos()
counter = 0


def add_todo():
    todo_ = st.session_state["add_todo"] + "\n"
    all_todos.append(todo_)
    write_todos(all_todos)


def delete_todo():
    pass


for i in all_todos:
    counter = counter + 1
st.title("Todo App")
st.subheader("List of Todos")

if counter == 0:
    st.write("Your todo list is empty....")
else:
    for todo in all_todos:
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            all_todos.remove(todo)
            write_todos(all_todos)
            del st.session_state[todo]
            st.experimental_rerun()
st.text_input(label=" ", placeholder="Add a todo....", on_change=add_todo, key="add_todo")
