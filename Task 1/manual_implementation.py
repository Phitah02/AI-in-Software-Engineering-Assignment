def sort_dictionaries_by_key(dict_list, sort_key):
    """
    Sort a list of dictionaries by a specific key using a manual bubble sort implementation.
    
    Args:
        dict_list (list): List of dictionaries to be sorted
        sort_key (str): Key to sort the dictionaries by
        
    Returns:
        list: Sorted list of dictionaries
    """
    # Create a copy of the input list to avoid modifying the original
    result = dict_list.copy()
    n = len(result)
    
    # Implement bubble sort manually
    for i in range(n):
        # Flag to optimize bubble sort
        swapped = False
        
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if result[j][sort_key] > result[j + 1][sort_key]:
                # Swap if they are in wrong order
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return result

# Example usage and test
if __name__ == "__main__":
    # Sample data
    people = [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Alice", "age": 25, "city": "London"},
        {"name": "Bob", "age": 35, "city": "Paris"},
        {"name": "Diana", "age": 28, "city": "Tokyo"}
    ]
    
    # Sort by different keys
    sorted_by_name = sort_dictionaries_by_key(people, "name")
    print("Sorted by name:", sorted_by_name)
    
    sorted_by_age = sort_dictionaries_by_key(people, "age")
    print("Sorted by age:", sorted_by_age)
    
    sorted_by_city = sort_dictionaries_by_key(people, "city")
    print("Sorted by city:", sorted_by_city)