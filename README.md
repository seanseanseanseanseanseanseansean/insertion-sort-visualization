# insertion-sort-visualization
Interactive insertion sort visualization using Python, Matplotlib, and Gradio.

Demo Videos:
[Download video](Full_sort_walkthrough.mp4)
[Download video](https://github.com/seanseanseanseanseanseanseansean/insertion-sort-visualization/blob/main/invalid_input_test.mp4)

Computational Thinking:

Computational Thinking: 
Decomposition: For the insertion sort algorithm, for each element starting with the smallest, we test whether the elemnt to the left is larger. If it is than the current elemnt is our of order and we swap those two elements. Then we test whether the one next to the new position is larger and so on. We do this for each element until we have sorted the last element and the list is sorted. 

Pattern recognition: Each step requires comparing adjacent elemnst, swpping smallest elemenst to the left, creating sorted section to the left until fully sorted.

Abstraction: The details I have decided to show the user are: the mechanics of the sorting algorithm through the animation itself, the different procceces that are repeated for each element (checking, swapping, inserted) and the fact that insertion sort happens in-place by simply swapping the elements in the same area rather than in a new region of the animation. Details that I have decided to leave out are the actual implementation of the code itself as I feel that that isn't important for the concept of insertion sort. 

Algorithm design: The user will input the length of the array that they wish to see in the animation and then click the "run" button. Once this happens, it will call the insertion sort function that outputs a figure at each frame displaying the current state of the sorting algorithm.

Flowchart: [(project_flowchart.pdf)](https://github.com/seanseanseanseanseanseanseansean/insertion-sort-visualization/blob/main/project_flowchart.pdf)


How to run:
Simply enter the number of elemnts you wish to see in the visualization, set the animation speed with the slider and click run to watch the animation.

Note: the program works perfectly well when run locally but for aome reason when the project is uploaded to huging face, the animation becomes very jittery. I don't know why this is but there isn't anything wrong with the code itself.

Hugging face link: https://huggingface.co/spaces/seanseanseanseanseansean/Insertion-Sort-Visualization


Author:
Sean Hughson
First-year general science student
Queen's University

Acknowledgments:
ChatGPT was used for this project for the following:
-Debugging small errors in my code: why my frames weren't showing up, why the coloring was offset
-Explaining basic syntax for gradio and matplotlib libraries: synatx for axes, figure, plots and legend functions
-Attempting to fix hugging face jitter, although nothing came of that

Other than that everything was done by me. All code was written by me and no ai code snippets were used. The only other resources I used was the documention from matplotlib.org and gradio.app
