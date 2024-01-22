def calculate_count(numbers):
    count = 0
    for _ in numbers:
        count += 1
    return count

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def calculate_mean(numbers):
    return calculate_sum(numbers) / calculate_count(numbers)

def calculate_std(numbers):
    mean = calculate_mean(numbers)
    squared_diff_sum = 0
    for number in numbers:
        squared_diff_sum += (number - mean) ** 2
    variance = squared_diff_sum / calculate_count(numbers)
    return (variance ** 0.5)

def calculate_min(numbers):
    min_val = numbers[0]
    for number in numbers:
        if number < min_val:
            min_val = number
    return min_val

def calculate_quarter(numbers):
    return calculate_count(numbers) / 4

def calculate_half(numbers):
    return calculate_count(numbers) / 2

def calculate_three_quarters(numbers):
    return calculate_count(numbers) * 3 / 4

def calculate_max(numbers):
    max_val = numbers[0]
    for number in numbers:
        if number > max_val:
            max_val = number
    return max_val