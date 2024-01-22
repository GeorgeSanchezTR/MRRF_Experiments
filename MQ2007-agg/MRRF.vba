Function RankValue(rank As Integer, c As Integer) As Double
    RankValue = 1 / (rank + c) ^ 2
End Function

Function Denom(c As Integer, n As Integer) As Double
  Dim sum_values As Double
  Dim i As Integer
  Dim rank_result As Double
  
  sum_values = 0
  For i = 1 To n Step 1
    rank_result = RankValue(i, c)
    sum_values = sum_values + rank_result
  Next i
  
  Denom = sum_values
End Function

Function MRRF(rank As Integer, c As Integer, n As Integer) As Double
    Dim denominator As Double
    Dim numerator As Double
    Dim result As Double
    
    denominator = Denom(c, n)
    numerator = RankValue(rank, c)
    result = numerator / denominator
    
    MRRF = result
End Function