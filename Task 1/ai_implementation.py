def sort_dictionaries_by_key(dict_list, sort_key):
    """
    Sort a list of dictionaries by a specific key using a more Pythonic approach.
    
    Args:
        dict_list (list): List of dictionaries to be sorted
        sort_key (str): Key to sort the dictionaries by
        
    Returns:
        list: Sorted list of dictionaries
    """
    # Using the sorted function with a lambda as key function
    # This is more efficient as it uses Python's built-in sorting algorithm (Timsort)
    return sorted(dict_list, key=lambda x: x[sort_key])

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