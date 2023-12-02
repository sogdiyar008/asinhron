# import asyncio
# import time
#
#
# async def async_func(task_no,ra):
#     print('///start', task_no)
#     await asyncio.sleep(ra)
#     print('///end', task_no)
#
# async def main():
#     task_list=[]
#     task1 = asyncio.create_task(async_func('A', 1))
#     task2 = asyncio.create_task(async_func('B', 2))
#     task3 = asyncio.create_task(async_func('C',3))
#
#     await asyncio.wait([task2, task3, task1])
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

# def multiply(a,b):
#     return a*b

import asyncio
import time
import httpx

# async def async_function(a):
#     while True:
#         await a
#         a +=1
#
# async_function(1)

# async def counter(count):
#     print(f'количество записей в списке {count}')
#     while True:
#         await asyncio.sleep(1/1000)
#         count.append(1)
#
# async def print_every_sec(count):
#     while True:
#         await asyncio.sleep(1)
#         print(f'- 1 sec passed. Count = {len(count)}')
#
# async def print_every_5sec():
#     while True:
#         await asyncio.sleep(5)
#         print('5 sec passed')
#
# async def print_every_10sec():
#     while True:
#         await asyncio.sleep(10)
#         print('10 sec passed')
#
# async def main():
#     count=list()
#     # task1=asyncio.create_task(counter(count))
#     # task2=asyncio.create_task(print_every_sec(count))
#     # task3=asyncio.create_task(print_every_5sec())
#     # task4=asyncio.create_task(print_every_10sec())
#     # await asyncio.wait([task1,task2,task3,task4])
#
#     task_list=[
#         counter(count),
#         print_every_sec(count),
#         print_every_5sec(),
#         print_every_10sec()
#     ]
#
#     await asyncio.gather(*task_list)
#
# asyncio.run(main())

# async def brew_cofee():
#     print('start brew coffee')
#     await asyncio.sleep(3)
#     print('finish brew coffee')
#     return 'coffee is ready'
#
# async def brew_Bage():
#     print('start brew Bage')
#     await asyncio.sleep(3)
#     print('finish brew Bage')
#     return 'Bage is ready'
#
# async def main():
#     start = time.time()
#
#     # batch = asyncio.gather(brew_Bage(), brew_cofee())
#     # result_coffee, result_toast = await batch
#
#     task_c=asyncio.create_task(brew_cofee())
#     task_t=asyncio.create_task(brew_Bage())
#     result_coffee = await task_c
#     result_toast = await task_t
#
#     end = time.time()
#
#     print(result_coffee)
#     print(result_toast)
#     print(f'spent time = {end - start:.2f} seconds')
#
# if __name__ == '__main__':
#     asyncio.run(main())


# async def my_sleep():
#     print('my sleep start')
#     await asyncio.sleep(2)
#     print('my sleep stop')
#
# async def main():
#     print('sleep now')
#     await my_sleep()
#     print('sleep stop')
#
# asyncio.run(main())


###############
###############
###############

# async def download(current_activity):
#     url = f'https://regres.in/api/users/{current_activity}'
#
#     async with httpx.AsyncClient() as client:
#         r=await client.get(url)
#         if r.status_code==200:
#             _r=r.json()
#             print(_r.get('data'))
#             r_dict=_r.get('data')
#             print(r_dict['first_name'])
#         else:
#             print(r.status_code)
#         print('рекомендую: ',current_activity)
#
#
# async def main():
#     page_count = int(input('сколько развлечений нужно?: '))
#
#     current_activity=0
#     while current_activity < page_count:
#         current_activity += 1
#         await download(current_activity)
#     print('Done')
#
# asyncio.run(main())


# async def Plus(a,b):
#     print('складывание началось')
#     await asyncio.sleep(5)
#     print('результат суммы', a+b)
#     return a+b
#
# async def kvadrat(a):
#     print('квадратирование началось')
#     await asyncio.sleep(2)
#     print('результат квадратирования', a**2)
#     return a**2
#
# async def main():
#     task1=asyncio.create_task(Plus(4,4))
#     task2=asyncio.create_task(kvadrat(4))
#
#     await asyncio.gather(task1, task2)
#
# asyncio.run(main())


# async def calls():
#     await asyncio.sleep(5)
#     print(f'Секретарь отвечает на вызовы \n-----') # ----- что бы пыло разлчимо от -- (типа по времени)
#
# async def takes():
#     await asyncio.sleep(5)
#     print(f'Секретарь принимает людей\n-----') # ----- что бы пыло разлчимо от -- (типа по времени)
#
# async def airlines():
#     await asyncio.sleep(2.5)
#     print('Секретарь разговаривает с авиакомпанией\n--') # ----- что бы пыло разлчимо от -- (типа по времени)
#
# async def grafics():
#     await asyncio.sleep(5)
#     print('Секретарь контролирует графики\n-----') # ----- что бы пыло разлчимо от -- (типа по времени)
#
# async def docs():
#     await asyncio.sleep(2.45)
#     print('Секретарь заполняет документы\n--') # ----- что бы пыло разлчимо от -- (типа по времени)
#
# async def main():
#     calls_task = asyncio.create_task(calls())
#     takes_task = asyncio.create_task(takes())
#     airlines_task = asyncio.create_task(airlines())
#     grafics_task = asyncio.create_task(grafics())
#     docs_task = asyncio.create_task(docs())
#
#     await asyncio.gather(calls_task, takes_task, airlines_task, grafics_task, docs_task)
#
# while True:
#     asyncio.run(main())

'''Я не особо понял что за чем должно идти, поэтому сделал так. ту все как по условию, онразговаривет по телефону и одновременно заполняет доки
но когда ему звонят, он перестает разговаривать с авикомпанией и отвечает на вызов. Так же перестает заполнять доки когда ему нужно принимать клиентов или же заполнять график'''