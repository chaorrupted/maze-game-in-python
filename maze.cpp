#include <iostream>
#include <vector>
#include <utility>

using namespace std;

void clearScreen() {
  cout << string(100,'\n');
}

void writeWalls(int board[13][13]) {
  vector <int> preset={1, 3, 1, 4, 1, 8, 2, 6, 2, 10, 3, 2, 3, 3, 3, 4, 3, 7, 3, 8, 3, 9, 3, 10, 4, 1, 4, 7, 5, 2, 5, 5, 5, 6, 5, 7, 5, 9, 5, 10, 5, 11, 6, 2, 6, 3, 6, 5, 7, 5, 7, 8, 7, 9, 7, 10, 8, 2, 8, 4, 8, 7, 8, 10, 9, 2, 9, 6, 9, 10, 10, 2, 10, 3, 10, 6, 10, 10, 11, 4, 11, 5};
  for (unsigned int i=0;i<preset.size();i+=2) {
    board[preset[i]][preset[i+1]]=1;
  }
}

void printBoard(int board[13][13], int size) {
  cout << endl << endl;
  for(int i=0;i<size;i++) {
    cout << "\t";
    for(int j=0;j<size;j++) {
      cout << " " << board[i][j];
    }
    cout << endl;
  }
}

int main() {
  int board[13][13]={0};
  for(int i=0;i<13;i++) {
    board[0][i]=1;
    board[12][i]=1;
    board[i][0]=1;
    board[i][12]=1;
  }
  pair<int,int> player={1,1};
  pair<int,int> target={8,8};
  board[player.first][player.second]=7;
  board[target.first][target.second]=8;
  writeWalls(board);

  cout << endl << "\t use a-s-d-f to move around and hit enter" << endl;
  char move;
  while(1) {
    //clearScreen();
    printBoard(board,13);
    if(player.first == target.first && player.second == target.second) {
      break;
    }
    cout << endl << endl << "\t to where: ";
    cin >> move;
    if(move == 's') {
      if(board[player.first+1][player.second] == 1) {
        cout << "\t that's a WALL over there!" << endl;
        continue;
      }
      else {
        cout << endl;
      }
      board[player.first][player.second]=0;
      player.first+=1;
      board[player.first][player.second]=7;
    }
    else if(move == 'w') {
      if(board[player.first-1][player.second] == 1) {
        cout << "\t that's a WALL over there!" << endl;
        continue;
      }
      else {
        cout << endl;
      }
      board[player.first][player.second]=0;
      player.first-=1;
      board[player.first][player.second]=7;
    }
    else if(move == 'd') {
      if(board[player.first][player.second+1] == 1) {
        cout << "\t that's a WALL over there!" << endl;
        continue;
      }
      else {
        cout << endl;
      }
      board[player.first][player.second]=0;
      player.second+=1;
      board[player.first][player.second]=7;
    }
    else if(move == 'a') {
      if(board[player.first][player.second-1] == 1) {
        cout << "\t that's a WALL over there!" << endl;
        continue;
      }
      else {
        cout << endl;
      }
      board[player.first][player.second]=0;
      player.second-=1;
      board[player.first][player.second]=7;
    }
    else {
      cout << "\t ?" << endl;
    }
  }
  while("banana") {
    int yay=rand() % 200;
    if(yay%2) {
      cout << "\t you did it" << endl;
    }
    else {
      cout << "\t CONGRATULATIONS" << endl;
    }
  }
  return 0;
}
