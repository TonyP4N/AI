import java.util.ArrayList;
import java.util.Arrays;

public class MoveChooser {
  
    public static Move chooseMove(BoardState boardState){

	    int searchDepth= Othello.searchDepth;
        int alpha = -9999;
        int beta = 9999;
        int best_value = -9999;
        ArrayList<Move> moves= boardState.getLegalMoves();
        BoardState boardState1 = boardState.deepCopy();
        Move bestMove = null;
        if(moves.isEmpty()) {
            return null;
        }

        for (Move move:moves) {
            boardState1.makeLegalMove(move.x, move.y);
            int value = AlphaBeta(boardState1, searchDepth, alpha, beta);
            if (value > best_value) {
                best_value = value;
                bestMove = move;
            }
        }
        return bestMove;

    }

    public static int AlphaBeta(BoardState boardState1, int depth, int alpha, int beta){
        BoardState boardState2 = boardState1.deepCopy();
        ArrayList<Move> moves2 = boardState1.getLegalMoves();
        int max = -9999;
        int min = 9999;
        if ((depth == 0) || moves2.isEmpty()){
            return countBoard(boardState1);
        }
        for (Move move:moves2) {
            boardState2.makeLegalMove(move.x, move.y);
            int value2 = AlphaBeta(boardState2, depth-1, alpha, beta);
            if (boardState2.colour == 1){
                if (value2 > alpha) {
                    if (value2 > beta) {
                        return value2;
                    }
                    else {
                        alpha = value2;
                    }
                }
                max = Math.max(alpha, value2);
            }

            else {
                if (value2 < beta) {
                    if (value2 < alpha) {
                        return value2;
                    }
                    else {
                        beta = value2;
                    }
                }
                min = Math.min(beta, value2);
            }

            if (alpha >= beta) {
                break;
            }
        }

        if (boardState1.colour == 1) {
            return max;
        }

        else {
            return min;
        }
    }

    public static int countBoard(BoardState boardState){
        int boardScore = 0;
        int [][] weight = {
                {120, -20, 20, 5, 5, 20, -20, 120},
                {-20, -40, -5, -5, -5, -5, -40, -20},
                {20, -5, 15, 3, 3, 15, -5, 20},
                {5, -5, 3, 3, 3, 3, -5, 5},
                {5, -5, 3, 3, 3, 3, -5, 5},
                {20, -5, 15, 3, 3, 15, -5, 20},
                {-20, -40, -5, -5, -5, -5, -40, -20},
                {120, -20, 20, 5, 5, 20, -20, 120}
        };
        for (int i=0; i<8; i++){
            for (int j=0; j<8; j++){
                if (boardState.colour == boardState.getContents(i,j)) {
                    boardScore +=  weight[i][j];
                }
                if (boardState.colour == -boardState.getContents(i,j)) {
                    boardScore -= weight[i][j];
                }
            }
        }
        return boardScore;
    }
}
