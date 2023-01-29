def scan(head, queue):
    total_cylinders = 0

    while queue:
        # Find the next request in the queue
        next_request = min(queue, key=lambda x: abs(x - head))

        print(f'Moving from {head} to {next_request}: {abs(next_request - head)} cylinders')
        total_cylinders += abs(next_request - head)
        head = next_request

        # Remove the request that we just serviced from the queue
        queue.remove(next_request)

    return total_cylinders

# Test SCAN algorithm
head = 97
queue = [1, 25, 53, 74, 13, 8, 63, 71, 14, 67]
print(f'SCAN total cylinders: {scan(head, queue)}')

def c_scan(head, queue):
    total_cylinders = 0
    max_cylinder = 199

    while queue:
        # Find the next request in the queue
        next_request = min(queue, key=lambda x: abs(x - head))

        # If the next request is on the other side of the disk, move the head to the other end first
        if next_request < head:
            print(f'Moving from {head} to {max_cylinder}: {max_cylinder - head} cylinders')
            total_cylinders += max_cylinder - head
            if head == max_cylinder:
                head = 0
            else:
                head = max_cylinder
            print(f'Moving from {head} to {next_request}: {next_request} cylinders')
            total_cylinders += next_request
        else:
            print(f'Moving from {head} to {next_request}: {next_request - head} cylinders')
            total_cylinders += next_request - head
            head = next_request

        # Remove the request that we just serviced from the queue
        queue

