import asyncio


async def worker(semaphore, i):
    await semaphore.acquire()
    print(f'Successfully acquired the Semaphore no: {i} !! ')
    await asyncio.sleep(2)
    print(f'Releasing the acquired Semaphore no : {i} !')
    semaphore.release()

async def main():
    loop = asyncio.get_running_loop()
    print(f'loop time : {loop.time()}')
    theSemaphore = asyncio.Semaphore(2)
    n = 5
    #worker_inputs = [worker(theSemaphore,i) for i in range(n)]
    worker_inputs = [worker(theSemaphore,1), worker(theSemaphore,2),worker(theSemaphore,3),worker(theSemaphore,4),worker(theSemaphore,5) ]
    print(worker_inputs)
    await asyncio.wait(worker_inputs)
    print('Finished all the workers !!')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("Loop has been completed ! ")
loop.close()



