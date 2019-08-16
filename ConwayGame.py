import numpy as np
import argparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 150
OFF = 0 
vals = [ON, OFF]

def setRandomGrid(N):
     return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N,N)

def findNeighbours(grid, i ,j, N):
     neighbours = int((grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, j] + grid[(i-1)%N, (j+1)%N] +
                       grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                       grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, j] + grid[(i+1)%N, (j+1)%N])/150)
     return neighbours

def update(frame, image, grid, N):
     newGrid = grid.copy()
     for i in range(N):
       for j in range(N):
          neighbours = findNeighbours(grid, i,j, N)
          if grid[i,j] == ON:
             if neighbours >3:
                newGrid[i,j] = OFF
             if neighbours < 2:
                newGrid[i,j] = OFF
          if grid[i,j] == OFF and neighbours == 3:
                newGrid[i,j] = ON
      
     image.set_data(newGrid)
     grid[:] = newGrid[:]
     return image

def main():

     parser = argparse.ArgumentParser(description="Runs Conway's Game of Life")

     parser.add_argument('--grid-size', dest='N', required=False)
     parser.add_argument('--interval', dest='interval', required = False)
     args = parser.parse_args()

     if args.N and int(args.N)>8:
         N = int(args.N)
     else:
         N = 100

     if args.interval:
         updateInterval = int(args.interval)
     else:
         updateInterval = 50
     
     grid = np.array([])
     grid = setRandomGrid(N)

     fig, ax = plt.subplots()
     image = ax.imshow(grid, interpolation='nearest')
     ani = animation.FuncAnimation(fig, update, fargs=(image, grid, N,  ), frames= 10, interval = updateInterval, save_count = 50)

     plt.title('Game of Life')
     plt.show() 

if __name__ == '__main__':
    main()

