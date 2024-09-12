from database import initialize_db, close_db
from models import Message

"""
def main():
    initialize_db()

    # Exemplo de criação de uma nova mensagem
    Message.create(
        action='SEND_MENSAGE',
        number='+5584988155454',
        message='Olá, esta é uma mensagem de teste!',
        status='PENDING'
    )

    # Exemplo de consulta
    messages = Message.select()
    for msg in messages:
        print(f"Action: {msg.action}, Number: {msg.number}, Status: {msg.status}")

    close_db()
"""

def insert_task(action, number, message, status):
    task_create = Message.create(
        action = action,
        number = number,
        message = message,
        status = status
    )
    return task_create

def update_status_task(task, new_status):
    task_return = Message.get_by_id(task)
    task_return.status = new_status
    task_return.save()
    return task_return

def delete_task_by_id(task: Message):
    Message.delete_by_id(task)
    print("TASK DELETADA COM SUCESSO")

def delete_all_tasks():
    Message.delete().execute()
    print("TODAS AS TAREFAS DELETADAS")

def get_tasks_list_by_status(status):
    tasks_return = Message.select().where(Message.status==status)
    return tasks_return

# if __name__ == '__main__':
#     main()

# initialize_db()

# nova_task = insert_task(
#     action="SEND_MENSAGE", 
#     number="+5584988155454",
#     message="Olá, esta é uma mensagem de teste!",
#     status="PENDING"
#     )

# print("Nova tarefa criada: ", nova_task.action)

# get_tasks = get_tasks_list_by_status("pending")
# print("TASKS PENDENTES ENCONTRADAS: ", len(get_tasks))

# task_select = get_tasks[0]
# print("MUDANÇA DE STATUS DE TASK SELECIONADA: ", task_select.action, " - ", task_select.status)
# update_status_task(task_select, "SUCCESS")
# print("MUDANÇA REALIZADA: ", task_select.action, " - ", task_select.status)

# delete_task_by_id(task_select)

# delete_all_tasks()

# close_db()