import gradio as gr

def selection_sort(arr):
    arr = arr.copy()  # avoid modifying the original list
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def sort_numbers(user_input):
    try:
        # Convert "3,1,2" into [3,1,2]
        num_list = [float(x.strip()) for x in user_input.split(",")]
    except:
        return "Error: please enter numbers separated by commas."

    sorted_list = selection_sort(num_list)
    return f"Sorted: {sorted_list}"

# Gradio Interface
demo = gr.Interface(
    fn=sort_numbers,
    inputs=gr.Textbox(label="Enter numbers separated by commas"),
    outputs=gr.Textbox(label="Sorted Output"),
    title="Selection Sort Visualizer",
    description="Enter a list of numbers and see them sorted using the Selection Sort algorithm."
)

demo.launch()
