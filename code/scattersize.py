In the scatterplot the s parameter determines the size of the dots. s can be a simple numeric value, say s=100, which will produce dots all of the same size. However you can pass a list of values (or a pandas Series) to provide sizes for the individual dots. This approach is very common as it allows us to provide an extra variable worth of information on the graph.


1. Modify the code we used for the scatter plot to include a size value for each of the points in the series being plotted. The downside is that some of the smaller dots may be completely covered by the larger dots. To try and highlight when this has happened we can change the opacity of the dots.


2. Find out which parameter controls the opacity of the dots ( clue - it is not called opacity), add it to you code and set it > to a reasonable value .