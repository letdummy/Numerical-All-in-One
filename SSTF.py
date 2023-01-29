head = 97
queue = [1, 25, 53, 74, 13, 8, 63, 71, 14, 67]
total_cylinders = 0

while queue:
    # Find the request that is closest to the current position of the head
    closest_request = min(queue, key=lambda x: abs(x - head))

    print(f'Moving from {head} to {closest_request}: {abs(closest_request - head)} cylinders')
    total_cylinders += abs(closest_request - head)
    head = closest_request

    # Remove the request that we just serviced from the queue
    queue.remove(closest_request)

print(f'Total cylinders moved: {total_cylinders}')
