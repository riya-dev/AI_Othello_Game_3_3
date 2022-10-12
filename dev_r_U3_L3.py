# Name: Riya Dev
# Date: 1/6/2021

import random
# updated 2

class RandomBot:
   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 8
      self.y_max = 8

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      
      ''' Your code goes here '''
      #best_move = [1, 1] # change this
      #return best_move, 0
      possible_moves = self.find_moves(board, color)
      x = random.choice(list(possible_moves))
      print(x)
      return (int(x / self.x_max), int(x % self.x_max)), 0
      
   def stones_left(self, board):
    # returns number of stones that can still be placed (empty spots)
      count = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == '.':
               count += 1
      return count

   def find_moves(self, board, color):
    # finds all possible moves
      moves_found = {}
      for i in range(len(board)):
         for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
               moves_found.update({i * self.y_max + j: flipped_stones})
      return moves_found

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
      if board[x][y] != ".":
         return []
      if color == self.black:
         color = "@"
      else:
         color = "O"
      flipped_stones = []
      for incr in self.directions:
         temp_flip = []
         x_pos = x + incr[0]
         y_pos = y + incr[1]
         while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
            if board[x_pos][y_pos] == ".":
               break
            if board[x_pos][y_pos] == color:
               flipped_stones += temp_flip
               break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
      return flipped_stones

class Best_AI_bot:

   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 8
      self.y_max = 8

   def best_strategy(self, board, color):
    # returns best move
      if color == "#ffffff": color = self.white
      else: color = self.black
      return self.minimax(board, color, 3)
      # return self.alphabeta(board, color, 3, -9999, 9999)
      # return best_move, 0

   def minimax(self, board, color, search_depth):
    # returns best "value"
      return self.max_value(board, color, search_depth)

   def max_value(self, board, color, search_depth):
      possible_moves = self.find_moves(board, color)
      best_move = (-1, -1)
   
      # print(color)
   
      if len(possible_moves) == 0: return (), -999
      #elif len(self.find_moves(board, self.opposite_color[color])) ==  0: return (), 999
      
      if search_depth == 1:
         return best_move, self.evaluate(board, color, possible_moves)
               
      val = -9999
      for m in possible_moves:
         move = (m // self.y_max, m % self.y_max)
         flipped = self.find_flipped(board, move[0], move[1], color)
         new_board = self.make_move(board, color, move, flipped)
         m, v = self.min_value(new_board, self.opposite_color[color], search_depth - 1)
         if v > val:
            val = v
            best_move = move
      return best_move, val
   
   def min_value(self, board, color, search_depth):
      possible_moves = self.find_moves(board, color)
      best_move = (-1, -1)
      
      if len(possible_moves) == 0: return (), 999 #best_move, 999
      #elif len(self.find_moves(board, self.opposite_color[color])) == 0: return (), -999
      
      if search_depth == 1:
         return best_move, self.evaluate(board, color, possible_moves)
         
      val = 9999
      for m in possible_moves:  
         move = (m // self.y_max, m % self.y_max)
         flipped = self.find_flipped(board, move[0], move[1], color)
         new_board = self.make_move(board, color, move, flipped)         
         m, v = self.max_value(new_board, self.opposite_color[color], search_depth - 1)
         if v < val:
            val = v
            best_move = move
      return best_move, val

   def negamax(self, board, color, search_depth):
    # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
    # returns best "value" while also pruning
      return self.ab_max_value(board, color, search_depth, alpha, beta)
   
   def ab_max_value(self, board, color, search_depth, alpha, beta):
      possible_moves = self.find_moves(board, color)
      best_move = (-1, -1)
      
      # terminal tests
      if len(possible_moves) == 0: return best_move, -999
      elif len(self.find_moves(board, self.opposite_color[color])) == 0: return best_move, 999
      if search_depth == 1:
         return best_move, self.evaluate(board, color, possible_moves)
     
      val = -9999
      for m in possible_moves:
         move = (m // self.y_max, m % self.y_max)
         flipped = self.find_flipped(board, move[0], move[1], color)
         new_board = self.make_move(board, color, move, flipped)
      
         val = max(val, self.ab_min_value(board, color, search_depth, alpha, beta), alpha, beta)
         if val > beta: return val # prune
         alpha = max(alpha, val)
      return best_move, val
   
   def ab_min_value(self, board, color, search_depth, alpha, beta):
      possible_moves = self.find_moves(board, color)
      best_move = (-1, -1)
      
      # terminal tests
      if len(possible_moves) == 0: return best_move, 999
      elif len(self.find_moves(board, self.opposite_color[color])) == 0: return best_move, -999
      if search_depth == 1:
         return best_move, self.evaluate(board, color, possible_moves)
     
      val = 9999
      for m in possible_moves:
         move = (m // self.y_max, m % self.y_max)
         flipped = self.find_flipped(board, move[0], move[1], color)
         new_board = self.make_move(board, color, move, flipped)
      
         val = min(val, self.ab_max_value(board, color, search_depth, alpha, beta), alpha, beta)
         if val < beta: return val # prune
         alpha = min(alpha, val)
      return best_move, val
         
   def make_key(self, board, color):
    # hashes the board
      return 1

   def stones_left(self, board):
    # returns number of stones that can still be placed
      count = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == '.':
               count += 1
      return count

   def make_move(self, board, color, move, flipped):
    # returns board that has been updated
      new_board = [x[:] for x in board] # deep copy
      new_board[move[0]][move[1]] = 'o' if color == self.white else '@'
      return new_board

   def evaluate(self, board, color, possible_moves):
    # returns the utility value
    
    # corners favorable
      score = [[30, -25, 10, 5, 5, 10, -25,  30,],
         [-25, -25,  1, 1, 1,  1, -25, -25,],
         [ 10,   1,  5, 2, 2,  5,   1,  10,],
         [  5,   1,  2, 1, 1,  2,   1,   5,],
         [  5,   1,  2, 1, 1,  2,   1,   5,],
         [ 10,   1,  5, 2, 2,  5,   1,  10,],
         [-25, -25,  1, 1, 1,  1, -25, -25,],
         [ 30, -25, 10, 5, 5, 10, -25,  30,],]
         
      ai_score = 0
      other_score = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == color:
               ai_score += score[i][j]
            elif board[i][j] == self.opposite_color[color]:
               other_score += score[i][j]
      return ai_score - other_score
      """         
      ai_count = 0
      other_count = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == color:
               ai_count += 1
            elif board[i][j] == self.opposite_color[color]:
               other_count += 1    
   
      return -100 * (ai_count - other_count)/(ai_count + other_count) # not working
      """
               
   def score(self, board, color):
    # returns the score of the board
      return 1

   def find_moves(self, board, color):
    # finds all possible moves
      moves_found = {}
      for i in range(len(board)):
         for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
               moves_found.update({i * self.y_max + j: flipped_stones})
      return moves_found

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
      if board[x][y] != ".":
         return []
      if color == self.black:
         color = "@"
      else:
         color = "O"
      flipped_stones = []
      for incr in self.directions:
         temp_flip = []
         x_pos = x + incr[0]
         y_pos = y + incr[1]
         while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
            if board[x_pos][y_pos] == ".":
               break
            if board[x_pos][y_pos] == color:
               flipped_stones += temp_flip
               break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
      return flipped_stones