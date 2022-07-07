import asyncio

async def mytasks1(task):
    print('Started task : task1 !! ')
    await asyncio.sleep(5)
    print('Completed task : task1 !! ')

async def mytasks2(task):
    print('Started task : task2 !! ')
    for i in range(10):
        print(i)
    print('Completed task : task2 !! ')    


async def main():
    # x = await mytasks1('task')
    # y = await mytasks2('task')

    x = asyncio.create_task(mytasks1('task'))
    y = asyncio.create_task(mytasks2('task'))

    await x
    await y
    print('completed both tasks !')

asyncio.run(main())
  
