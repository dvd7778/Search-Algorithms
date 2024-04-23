import search


X = "Block"
S = "Start"
G = "Goal"
         # 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # A
          [0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, X, X, X, 0, 0, 0, X, X, X, X, X, X, X, 0, 0, 0, X, 0, 0, 0, G, 0, 0], # B
          [0, 0, 0, 0, 0, X, X, X, 0, 0, 0, 0, 0, 0, 0, 0, X, X, X, X, X, 0, 0, X, X, X, X, X, X, X, 0, 0, X, X, X, 0, 0, 0, 0, 0], # C
          [0, 0, 0, 0, X, X, X, X, X, 0, 0, 0, 0, 0, 0, 0, X, X, X, X, X, X, 0, X, X, X, X, X, X, X, 0, X, X, X, X, X, 0, 0, 0, 0], # D
          [0, 0, 0, X, X, X, X, X, X, X, 0, 0, 0, 0, 0, 0, X, X, X, X, X, 0, 0, X, X, X, X, X, X, X, 0, X, X, X, X, X, 0, 0, 0, 0], # E
          [0, 0, X, X, X, X, X, X, X, X, X, 0, 0, X, 0, 0, X, X, X, X, 0, 0, 0, X, X, X, X, X, X, X, 0, X, X, X, X, X, 0, 0, 0, 0], # F
          [0, 0, X, X, X, X, X, X, X, X, 0, 0, X, X, X, 0, X, X, 0, 0, 0, 0, 0, X, X, X, X, X, X, X, 0, 0, X, X, X, X, 0, 0, 0, 0], # G
          [0, 0, 0, X, X, X, X, X, X, X, 0, 0, X, X, X, 0, 0, 0, 0, 0, 0, 0, 0, X, X, X, X, X, X, X, 0, 0, X, X, X, 0, 0, 0, 0, 0], # H
          [0, 0, 0, X, X, X, X, X, X, X, 0, X, X, X, X, X, 0, 0, 0, 0, 0, 0, 0, X, X, X, X, X, X, X, 0, 0, 0, X, X, 0, 0, 0, 0, 0], # I
          [0, 0, 0, X, X, X, X, X, X, 0, 0, X, X, X, X, X, 0, 0, 0, 0, 0, 0, 0, X, X, X, X, X, X, X, 0, 0, 0, X, X, 0, 0, 0, 0, 0], # J
          [0, 0, 0, 0, X, X, X, X, X, 0, X, X, X, X, X, X, X, 0, 0, X, X, 0, 0, X, X, X, X, X, X, X, 0, 0, 0, X, X, 0, 0, 0, 0, 0], # K
          [0, 0, 0, 0, 0, 0, X, X, 0, 0, X, X, X, X, X, X, X, 0, 0, X, X, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, X, 0, 0, 0, 0, 0], # L
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, X, X, X, 0, 0, 0, 0, 0, X, X, X, X, X, 0, 0, 0, 0, 0, 0, 0], # M
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, X, X, X, 0, 0, 0, X, X, X, X, X, X, X, 0, 0, 0, 0, 0, 0], # N
          [0, 0, 0, 0, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, 0, X, X, X, X, X, 0, 0, X, X, X, X, X, X, X, 0, 0, 0, 0, 0, 0], # O
          [0, 0, 0, 0, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, 0, X, X, X, X, 0, 0, 0, X, X, X, X, X, X, X, 0, 0, 0, 0, 0, 0], # P
          [0, 0, 0, 0, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, 0, 0, X, X, 0, 0, 0, 0, X, X, X, X, X, X, X, 0, 0, 0, 0, 0, 0], # Q
          [0, 0, S, 0, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, 0, 0, X, 0, 0, 0, 0, 0, 0, X, X, X, X, X, 0, 0, 0, 0, 0, 0, 0], # R
          [0, 0, 0, 0, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, X, 0, 0, 0, 0, 0, 0, 0, 0], # S
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] # T

def get_graph_dict():
   
   graph_dict = {  
                  "A1" : {"B1" : 1, "A2" : 1}, 
                  "A2" : {"A1" : 1, "A3" : 1, "B2" : 1},
                  "A3" : {"A2" : 1, "A4" : 1, "B3" : 1},
                  "A4" : {"A3" : 1, "A5" : 1, "B4" : 1},
                  "A5" : {"A4" : 1, "A6" : 1, "B5" : 1},
                  "A6" : {"A5" : 1, "A7" : 1, "B6" : 1},
                  "A7" : {"A6" : 1, "A8" : 1},
                  "A8" : {"A7" : 1, "A9" : 1, "B8" : 1},
                  "A9" : {"A8" : 1, "A10" : 1, "B9" : 1},
                  "A10" : {"A9" : 1, "A11" : 1, "B10" : 1},
                  "A11" : {"A10" : 1, "A12" : 1, "B11" : 1},
                  "A12" : {"A11" : 1, "A13" : 1, "B12" : 1},
                  "A13" : {"A12" : 1, "A14" : 1, "B13" : 1},
                  "A14" : {"A13" : 1, "A15" : 1, "B14" : 1},
                  "A15" : {"A14" : 1, "A16" : 1, "B15" : 1},
                  "A16" : {"A15" : 1, "A17" : 1, "B16" : 1},
                  "A17" : {"A16" : 1, "A18" : 1},
                  "A18" : {"A17" : 1, "A19" : 1},
                  "A19" : {"A18" : 1, "A20" : 1},
                  "A20" : {"A19" : 1, "A21" : 1},
                  "A21" : {"A20" : 1, "A22" : 1, "B21" : 1},
                  "A22" : {"A21" : 1, "A23" : 1, "B22" : 1},
                  "A23" : {"A22" : 1, "A24" : 1, "B23" : 1},
                  "A24" : {"A23" : 1, "A25" : 1},
                  "A25" : {"A24" : 1, "A26" : 1},
                  "A26" : {"A25" : 1, "A27" : 1},
                  "A27" : {"A26" : 1, "A28" : 1},
                  "A28" : {"A27" : 1, "A29" : 1},
                  "A29" : {"A28" : 1, "A30" : 1},
                  "A30" : {"A29" : 1, "A31" : 1},
                  "A31" : {"A30" : 1, "A32" : 1, "B31" : 1},
                  "A32" : {"A31" : 1, "A33" : 1, "B32" : 1},
                  "A33" : {"A32" : 1, "A34" : 1, "B33" : 1},
                  "A34" : {"A33" : 1, "A35" : 1},
                  "A35" : {"A34" : 1, "A36" : 1, "B35" : 1},
                  "A36" : {"A35" : 1, "A37" : 1, "B36" : 1},
                  "A37" : {"A36" : 1, "A38" : 1, "B37" : 1},
                  "A38" : {"A37" : 1, "A39" : 1, "B38" : 1},
                  "A39" : {"A38" : 1, "A40" : 1, "B39" : 1},
                  "A40" : {"A39" : 1, "B40" : 1},
                  "B1" : {"A1" : 1, "B2" : 1, "C1" : 1},
                  "B2" : {"A2" : 1, "B1" : 1, "B3" : 1, "C2" : 1},
                  "B3" : {"A3" : 1, "B2" : 1, "B4" : 1, "C3" : 1},
                  "B4" : {"A4" : 1, "B3" : 1, "B5" : 1, "C4" : 1},
                  "B5" : {"A5" : 1, "B4" : 1, "B6" : 1, "C5" : 1},
                  "B6" : {"A6" : 1, "B5" : 1},
                  "B8" : {"A8" : 1, "B9" : 1},
                  "B9" : {"A9" : 1, "B8" : 1, "B10" : 1, "C9" : 1},
                  "B10" : {"A10" : 1, "B9" : 1, "B11" : 1, "C10" : 1},
                  "B11" : {"A11" : 1, "B10" : 1, "B12" : 1, "C11" : 1},
                  "B12" : {"A12" : 1, "B11" : 1, "B13" : 1, "C12" : 1},
                  "B13" : {"A13" : 1, "B12" : 1, "B14" : 1, "C13" : 1},
                  "B14" : {"A14" : 1, "B13" : 1, "B15" : 1, "C14" : 1},
                  "B15" : {"A15" : 1, "B14" : 1, "B16" : 1, "C15" : 1},
                  "B16" : {"A16" : 1, "B15" : 1, "C16" : 1},
                  "B21" : {"A21" : 1, "B22" : 1},
                  "B22" : {"A22" : 1, "B21" : 1, "B23" : 1, "C22" : 1},
                  "B23" : {"A23" : 1, "B22" : 1, "C23" : 1},
                  "B31" : {"A31" : 1, "B32" : 1, "C31" : 1},
                  "B32" : {"A32" : 1, "B21" : 1, "B33" : 1, "C32" : 1},
                  "B33" : {"A33" : 1, "B32" : 1},
                  "B35" : {"A35" : 1, "B36" : 1},
                  "B36" : {"A36" : 1, "B35" : 1, "B36" : 1, "C36" : 1},
                  "B37" : {"A37" : 1, "B36" : 1, "B37" : 1, "C37" : 1},
                  "B38" : {"A38" : 1, "B37" : 1, "B38" : 1, "C38" : 1},
                  "B39" : {"A39" : 1, "B38" : 1, "B39" : 1, "C39" : 1},
                  "B40" : {"A40" : 1, "B39" : 1, "C40" : 1},
                  "C1" : {"B1" : 1, "C2" : 1, "D1" : 1},
                  "C2" : {"B2" : 1, "C1" : 1, "C3" : 1, "D2" : 1},
                  "C3" : {"B3" : 1, "C2" : 1, "C4" : 1, "D3" : 1},
                  "C4" : {"B4" : 1, "C3" : 1, "C5" : 1, "D4" : 1},
                  "C5" : {"B5" : 1, "C4" : 1},
                  "C9" : {"B9" : 1, "C10" : 1},
                  "C10" : {"B10" : 1, "C9" : 1, "C11" : 1, "D10" : 1},
                  "C11" : {"B11" : 1, "C10" : 1, "C12" : 1, "D11" : 1},
                  "C12" : {"B12" : 1, "C11" : 1, "C13" : 1, "D12" : 1},
                  "C13" : {"B13" : 1, "C12" : 1, "C14" : 1, "D13" : 1},
                  "C14" : {"B14" : 1, "C13" : 1, "C15" : 1, "D14" : 1},
                  "C15" : {"B15" : 1, "C14" : 1, "C16" : 1, "D15" : 1},
                  "C16" : {"B16" : 1, "C15" : 1, "D16" : 1},
                  "C22" : {"B22" : 1, "C23" : 1},
                  "C23" : {"B23" : 1, "C22" : 1, "D23" : 1},
                  "C31" : {"B31" : 1, "C32" : 1, "D31" : 1},
                  "C32" : {"B32" : 1, "C31" : 1},
                  "C36" : {"B36" : 1, "C37" : 1},
                  "C37" : {"B37" : 1, "C36" : 1, "C38" : 1, "D12" : 1},
                  "C38" : {"B38" : 1, "C37" : 1, "C39" : 1, "D13" : 1},
                  "C39" : {"B39" : 1, "C38" : 1, "C40" : 1, "D14" : 1},
                  "C40" : {"B40" : 1, "C39" : 1, "D40" : 1},
                  "D1" : {"C1" : 1, "D2" : 1, "E1" : 1},
                  "D2" : {"C2" : 1, "D1" : 1, "D3" : 1, "E2" : 1},
                  "D3" : {"C3" : 1, "D2" : 1, "D4" : 1, "E3" : 1},
                  "D4" : {"C4" : 1, "D3" : 1},
                  "D10" : {"C10" : 1, "D11" : 1},
                  "D11" : {"C11" : 1, "D10" : 1, "D12" : 1, "E11" : 1},
                  "D12" : {"C12" : 1, "D11" : 1, "D13" : 1, "E12" : 1},
                  "D13" : {"C13" : 1, "D12" : 1, "D14" : 1, "E13" : 1},
                  "D14" : {"C14" : 1, "D13" : 1, "D15" : 1, "E14" : 1},
                  "D15" : {"C15" : 1, "D14" : 1, "D16" : 1, "E15" : 1},
                  "D16" : {"C16" : 1, "D15" : 1, "E16" : 1},
                  "D23" : {"C23" : 1, "E23" : 1},
                  "D31" : {"C31" : 1, "E31" : 1},
                  "D37" : {"C37" : 1, "D38" : 1, "E37" : 1},
                  "D38" : {"C38" : 1, "D37" : 1, "D39" : 1, "E38" : 1},
                  "D39" : {"C39" : 1, "D38" : 1, "D40" : 1, "E39" : 1},
                  "D40" : {"C40" : 1, "D39" : 1, "E40" : 1},
                  "E1" : {"D1" : 1, "E2" : 1, "F1" : 1},
                  "E2" : {"D2" : 1, "E1" : 1, "E3" : 1, "F2" : 1},
                  "E3" : {"D3" : 1, "E2" : 1},
                  "E11" : {"D11" : 1, "E12" : 1},
                  "E12" : {"D12" : 1, "E11" : 1, "E13" : 1, "F12" : 1},
                  "E13" : {"D13" : 1, "E12" : 1, "E14" : 1, "F13" : 1},
                  "E14" : {"D14" : 1, "E13" : 1, "E15" : 1},
                  "E15" : {"D15" : 1, "E14" : 1, "E16" : 1, "F15" : 1},
                  "E16" : {"D16" : 1, "E15" : 1, "F16" : 1},
                  "E22" : {"E23" : 1, "F22" : 1},
                  "E23" : {"D23" : 1, "E22" : 1, "F23" : 1},
                  "E31" : {"D31" : 1, "F31" : 1},
                  "E37" : {"D37" : 1, "E38" : 1, "F37" : 1},
                  "E38" : {"D38" : 1, "E37" : 1, "E39" : 1, "F38" : 1},
                  "E39" : {"D39" : 1, "E38" : 1, "E40" : 1, "F39" : 1},
                  "E40" : {"D40" : 1, "E39" : 1, "F40" : 1},
                  "F1" : {"E1" : 1, "F2" : 1, "G1" : 1},
                  "F2" : {"E2" : 1, "F1" : 1, "G2" : 1},
                  "F12" : {"E12" : 1, "F13" : 1, "G12" : 1},
                  "F13" : {"E13" : 1, "F12" : 1},
                  "F15" : {"E15" : 1, "F16" : 1},
                  "F16" : {"E16" : 1, "F15" : 1, "G16" : 1},
                  "F21" : {"F22" : 1, "G21" : 1},
                  "F22" : {"E22" : 1, "F21" : 1, "F23" : 1, "G22" : 1},
                  "F23" : {"E23" : 1, "F22" : 1, "G23" : 1},
                  "F31" : {"E31" : 1, "G31" : 1},
                  "F37" : {"E37" : 1, "F38" : 1, "G37" : 1},
                  "F38" : {"E38" : 1, "F37" : 1, "F39" : 1, "G38" : 1},
                  "F39" : {"E39" : 1, "F38" : 1, "F40" : 1, "G39" : 1},
                  "F40" : {"E40" : 1, "F39" : 1, "G40" : 1},
                  "G1" : {"F1" : 1, "G2" : 1, "H1" : 1},
                  "G2" : {"F2" : 1, "G1" : 1, "H2" : 1},
                  "G11" : {"G12" : 1, "H11" : 1},
                  "G12" : {"F12" : 1, "G11" : 1, "H12" : 1},
                  "G16" : {"F16" : 1, "H16" : 1},
                  "G19" : {"G20" : 1, "H19" : 1},
                  "G20" : {"G19" : 1, "G21" : 1, "H20" : 1},
                  "G21" : {"F21" : 1, "G20" : 1, "G22" : 1, "H21" : 1},
                  "G22" : {"F22" : 1, "G21" : 1, "G23" : 1, "H22" : 1},
                  "G23" : {"F23" : 1, "G22" : 1, "H23" : 1},
                  "G31" : {"F31" : 1, "G32" : 1, "H31" : 1},
                  "G32" : {"G31" : 1, "H32" : 1},
                  "G37" : {"F37" : 1, "G38" : 1, "H37" : 1},
                  "G38" : {"F38" : 1, "G37" : 1, "G39" : 1, "H38" : 1},
                  "G39" : {"F39" : 1, "G38" : 1, "G40" : 1, "H39" : 1},
                  "G40" : {"F40" : 1, "G39" : 1, "H40" : 1},
                  "H1" : {"G1" : 1, "H2" : 1, "I1" : 1},
                  "H2" : {"G2" : 1, "H1" : 1, "H3" : 1, "I2" : 1},
                  "H3" : {"H2" : 1, "I3" : 1},
                  "H11" : {"G11" : 1, "H12" : 1, "I11" : 1},
                  "H12" : {"G12" : 1, "H11" : 1},
                  "H16" : {"G16" : 1, "H17" : 1},
                  "H17" : {"H16" : 1, "H18" : 1, "I17" : 1},
                  "H18" : {"H17" : 1, "H19" : 1, "I18" : 1},
                  "H19" : {"G19" : 1, "H18" : 1, "H20" : 1, "I19" : 1},
                  "H20" : {"G20" : 1, "H19" : 1, "H21" : 1, "I20" : 1},
                  "H21" : {"G21" : 1, "H20" : 1, "H22" : 1, "I21" : 1},
                  "H22" : {"G22" : 1, "H21" : 1, "H23" : 1, "I22" : 1},
                  "H23" : {"G23" : 1, "H22" : 1, "I23" : 1},
                  "H31" : {"G31" : 1, "H32" : 1, "I31" : 1},
                  "H32" : {"G32" : 1, "H31" : 1, "I32" : 1},
                  "H36" : {"H37" : 1, "I36" : 1},
                  "H37" : {"G37" : 1, "H36" : 1, "H38" : 1, "I37" : 1},
                  "H38" : {"G38" : 1, "H37" : 1, "H39" : 1, "I38" : 1},
                  "H39" : {"G39" : 1, "H38" : 1, "H40" : 1, "I39" : 1},
                  "H40" : {"G40" : 1, "H39" : 1, "I40" : 1},
                  "I1" : {"H1" : 1, "I2" : 1, "J1" : 1},
                  "I2" : {"H2" : 1, "I1" : 1, "I3" : 1, "J2" : 1},
                  "I3" : {"H3" : 1, "I2" : 1, "J3" : 1},
                  "I11" : {"H11" : 1, "J11" : 1},
                  "I17" : {"H17" : 1, "I18" : 1, "J17" : 1},
                  "I18" : {"H18" : 1, "I17" : 1, "I19" : 1, "J18" : 1},
                  "I19" : {"H19" : 1, "I18" : 1, "I20" : 1, "J19" : 1},
                  "I20" : {"H20" : 1, "I19" : 1, "I21" : 1, "J20" : 1},
                  "I21" : {"H21" : 1, "I20" : 1, "I22" : 1, "J21" : 1},
                  "I22" : {"H22" : 1, "I21" : 1, "I23" : 1, "J22" : 1},
                  "I23" : {"H23" : 1, "I22" : 1, "J23" : 1},
                  "I31" : {"H31" : 1, "I32" : 1, "J31" : 1},
                  "I32" : {"H32" : 1, "I31" : 1, "I33" : 1, "J32" : 1},
                  "I33" : {"I32" : 1, "J33" : 1},
                  "I36" : {"H36" : 1, "I37" : 1, "J36" : 1},
                  "I37" : {"H37" : 1, "I38" : 1, "I36" : 1, "J37" : 1},
                  "I38" : {"H38" : 1, "I39" : 1, "I37" : 1, "J38" : 1},
                  "I39" : {"H39" : 1, "I40" : 1, "I38" : 1, "J39" : 1},
                  "I40" : {"H40" : 1, "I39" : 1, "J40" : 1},
                  "J1" : {"I1" : 1, "J2" : 1, "K1" : 1},
                  "J2" : {"I2" : 1, "J1" : 1, "J3" : 1, "K2" : 1},
                  "J3" : {"I3" : 1, "J2" : 1, "K3" : 1},
                  "J10" : {"J11" : 1, "K10" : 1},
                  "J11" : {"I11" : 1, "J10" : 1},
                  "J17" : {"I17" : 1, "J18" : 1},
                  "J18" : {"I18" : 1, "J17" : 1, "J19" : 1, "K18" : 1},
                  "J19" : {"I19" : 1, "J18" : 1, "J20" : 1, "K19" : 1},
                  "J20" : {"I20" : 1, "J19" : 1, "J21" : 1},
                  "J21" : {"I21" : 1, "J20" : 1, "J22" : 1},
                  "J22" : {"I22" : 1, "J21" : 1, "J23" : 1, "K22" : 1},
                  "J23" : {"I23" : 1, "J22" : 1, "K23" : 1},
                  "J31" : {"I31" : 1, "J32" : 1, "K31" : 1},
                  "J32" : {"I32" : 1, "J31" : 1, "J33" : 1, "K32" : 1},
                  "J33" : {"I33" : 1, "J32" : 1, "K33" : 1},
                  "J36" : {"I36" : 1, "J37" : 1, "K36" : 1},
                  "J37" : {"I37" : 1, "J36" : 1, "J38" : 1, "K37" : 1},
                  "J38" : {"I38" : 1, "J37" : 1, "J39" : 1, "K38" : 1},
                  "J39" : {"I39" : 1, "J38" : 1, "J40" : 1, "K39" : 1},
                  "J40" : {"I40" : 1, "J39" : 1, "K40" : 1},
                  "K1" : {"J1" : 1, "K2" : 1, "L1" : 1},
                  "K2" : {"J2" : 1, "K1" : 1, "K3" : 1, "L2" : 1},
                  "K3" : {"J3" : 1, "K2" : 1, "K4" : 1, "L3" : 1},
                  "K4" : {"K3" : 1, "L4" : 1},
                  "K10" : {"J10" : 1, "L10" : 1},
                  "K18" : {"J18" : 1, "K19" : 1, "L18" : 1},
                  "K19" : {"J19" : 1, "K18" : 1, "L19" : 1},
                  "K22" : {"J22" : 1, "K23" : 1},
                  "K23" : {"J23" : 1, "K22" : 1, "L23" : 1},
                  "K31" : {"J31" : 1, "K32" : 1, "L31" : 1},
                  "K32" : {"J32" : 1, "K31" : 1, "K33" : 1},
                  "K33" : {"J33" : 1, "K32" : 1, "L33" : 1},
                  "K36" : {"J36" : 1, "K37" : 1, "L36" : 1},
                  "K37" : {"J37" : 1, "K36" : 1, "K38" : 1, "L37" : 1},
                  "K38" : {"J38" : 1, "K37" : 1, "K39" : 1, "L38" : 1},
                  "K39" : {"J39" : 1, "K38" : 1, "K40" : 1, "L39" : 1},
                  "K40" : {"J40" : 1, "K39" : 1, "L40" : 1},
                  "L1" : {"K1" : 1, "L2" : 1, "M1" : 1},
                  "L2" : {"K2" : 1, "L1" : 1, "L3" : 1, "M2" : 1},
                  "L3" : {"K3" : 1, "L2" : 1, "L4" : 1, "M3" : 1},
                  "L4" : {"K4" : 1, "L3" : 1, "L5" : 1, "M4" : 1},
                  "L5" : {"L4" : 1, "L6" : 1, "M5" : 1},
                  "L6" : {"L5" : 1, "M6" : 1},
                  "L9" : {"L10" : 1, "M9" : 1},
                  "L10" : {"K10" : 1, "L9" : 1, "M10" : 1},
                  "L18" : {"K18" : 1, "L19" : 1, "M18" : 1},
                  "L19" : {"K19" : 1, "L18" : 1, "M19" : 1},
                  "L23" : {"K23" : 1, "L24" : 1},
                  "L24" : {"L23" : 1, "L25" : 1, "M24" : 1},
                  "L25" : {"L24" : 1, "L26" : 1, "M25" : 1},
                  "L26" : {"L25" : 1, "L27" : 1, "M26" : 1},
                  "L27" : {"L26" : 1, "L28" : 1, "M27" : 1},
                  "L28" : {"L27" : 1, "L29" : 1, "M28" : 1},
                  "L29" : {"L28" : 1, "L30" : 1},
                  "L30" : {"L29" : 1, "L31" : 1},
                  "L31" : {"K31" : 1, "L30" : 1},
                  "L33" : {"K33" : 1, "L34" : 1},
                  "L34" : {"L33" : 1, "M34" : 1},
                  "L36" : {"K36" : 1, "L37" : 1, "M36" : 1},
                  "L37" : {"K37" : 1, "L36" : 1, "L38" : 1, "M37" : 1},
                  "L38" : {"K38" : 1, "L37" : 1, "L39" : 1, "M38" : 1},
                  "L39" : {"K39" : 1, "L38" : 1, "L40" : 1, "M39" : 1},
                  "L40" : {"K40" : 1, "L39" : 1, "M40" : 1},
                  "M1" : {"L1" : 1, "M2" : 1, "N1" : 1},
                  "M2" : {"L2" : 1, "M1" : 1, "M3" : 1, "N2" : 1},
                  "M3" : {"L3" : 1, "M2" : 1, "M4" : 1, "N3" : 1},
                  "M4" : {"L4" : 1, "M3" : 1, "M5" : 1, "N4" : 1},
                  "M5" : {"L5" : 1, "M4" : 1, "M6" : 1, "N5" : 1},
                  "M6" : {"L6" : 1, "M5" : 1, "M7" : 1, "N6" : 1},
                  "M7" : {"M6" : 1, "M8" : 1, "N7" : 1},
                  "M8" : {"M7" : 1, "M9" : 1, "N8" : 1},
                  "M9" : {"L9" : 1, "M8" : 1, "M10" : 1, "N9" : 1},
                  "M10" : {"L10" : 1, "M9" : 1, "M11" : 1, "N10" : 1},
                  "M11" : {"M10" : 1, "M12" : 1, "N11" : 1},
                  "M12" : {"M11" : 1, "M13" : 1, "N12" : 1},
                  "M13" : {"M12" : 1, "M14" : 1, "N13" : 1},
                  "M14" : {"M13" : 1, "M15" : 1, "N14" : 1},
                  "M15" : {"M14" : 1, "M16" : 1, "N15" : 1},
                  "M16" : {"M15" : 1, "M17" : 1, "N16" : 1},
                  "M17" : {"M16" : 1, "M18" : 1, "N17" : 1},
                  "M18" : {"L18" : 1, "M17" : 1, "M19" : 1, "N18" : 1},
                  "M19" : {"L19" : 1, "M18" : 1, "N19" : 1},
                  "M24" : {"L24" : 1, "M25" : 1},
                  "M25" : {"L25" : 1, "M24" : 1, "M26" : 1, "N25" : 1},
                  "M26" : {"L26" : 1, "M25" : 1, "M27" : 1, "N26" : 1},
                  "M27" : {"L27" : 1, "M26" : 1, "M28" : 1, "N27" : 1},
                  "M28" : {"L28" : 1, "M27" : 1},
                  "M34" : {"L34" : 1, "M35" : 1},
                  "M35" : {"M34" : 1, "M36" : 1, "N35" : 1},
                  "M36" : {"L36" : 1, "M35" : 1, "M37" : 1, "N36" : 1},
                  "M37" : {"L37" : 1, "M36" : 1, "M38" : 1, "N37" : 1},
                  "M38" : {"L38" : 1, "M37" : 1, "M39" : 1, "N38" : 1},
                  "M39" : {"L39" : 1, "M38" : 1, "M40" : 1, "N39" : 1},
                  "M40" : {"L40" : 1, "M39" : 1, "N40" : 1},
                  "N1" : {"M1" : 1, "N2" : 1, "O1" : 1},
                  "N2" : {"M2" : 1, "N1" : 1, "N3" : 1, "O2" : 1},
                  "N3" : {"M3" : 1, "N2" : 1, "N4" : 1, "O3" : 1},
                  "N4" : {"M4" : 1, "N3" : 1, "N5" : 1, "O4" : 1},
                  "N5" : {"M5" : 1, "N4" : 1, "N6" : 1},
                  "N6" : {"M6" : 1, "N5" : 1, "N7" : 1},
                  "N7" : {"M7" : 1, "N6" : 1, "N8" : 1},
                  "N8" : {"M8" : 1, "N7" : 1, "N9" : 1},
                  "N9" : {"M9" : 1, "N8" : 1, "N10" : 1},
                  "N10" : {"M10" : 1, "N9" : 1, "N11" : 1},
                  "N11" : {"M11" : 1, "N10" : 1, "N12" : 1},
                  "N12" : {"M12" : 1, "N11" : 1, "N13" : 1},
                  "N13" : {"M13" : 1, "N12" : 1, "N14" : 1},
                  "N14" : {"M14" : 1, "N13" : 1, "N15" : 1},
                  "N15" : {"M15" : 1, "N14" : 1, "N16" : 1},
                  "N16" : {"M16" : 1, "N15" : 1, "N17" : 1},
                  "N17" : {"M17" : 1, "N16" : 1, "N18" : 1},
                  "N18" : {"M18" : 1, "N17" : 1, "N19" : 1},
                  "N19" : {"M19" : 1, "N18" : 1, "N20" : 1},
                  "N20" : {"N19" : 1, "O20" : 1},
                  "N25" : {"M25" : 1, "N26" : 1},
                  "N26" : {"M26" : 1, "N25" : 1, "N27" : 1, "O26" : 1},
                  "N27" : {"M27" : 1, "N26" : 1, "O27" : 1},
                  "N35" : {"M35" : 1, "N36" : 1, "O35" : 1},
                  "N36" : {"M36" : 1, "N35" : 1, "N37" : 1, "O36" : 1},
                  "N37" : {"M37" : 1, "N36" : 1, "N38" : 1, "O37" : 1},
                  "N38" : {"M38" : 1, "N37" : 1, "N39" : 1, "O38" : 1},
                  "N39" : {"M39" : 1, "N38" : 1, "N40" : 1, "O39" : 1},
                  "N40" : {"M40" : 1, "N39" : 1, "O40" : 1},
                  "O1" : {"N1" : 1, "O2" : 1, "P1" : 1},
                  "O2" : {"N2" : 1, "O1" : 1, "O3" : 1, "P2" : 1},
                  "O3" : {"N3" : 1, "O2" : 1, "O4" : 1, "P3" : 1},
                  "O4" : {"N4" : 1, "O3" : 1, "P4" : 1},
                  "O20" : {"N20" : 1, "P20" : 1},
                  "O26" : {"N26" : 1, "O27" : 1, "P26" : 1},
                  "O27" : {"N27" : 1, "O26" : 1, "P27" : 1},
                  "O35" : {"N35" : 1, "O36" : 1, "P35" : 1},
                  "O36" : {"N36" : 1, "O35" : 1, "O37" : 1, "P36" : 1},
                  "O37" : {"N37" : 1, "O36" : 1, "O38" : 1, "P37" : 1},
                  "O38" : {"N38" : 1, "O37" : 1, "O39" : 1, "P38" : 1},
                  "O39" : {"N39" : 1, "O38" : 1, "O40" : 1, "P39" : 1},
                  "O40" : {"N40" : 1, "O39" : 1, "P40" : 1},
                  "P1" : {"O1" : 1, "P2" : 1, "Q1" : 1},
                  "P2" : {"O2" : 1, "P1" : 1, "P3" : 1, "Q2" : 1},
                  "P3" : {"O3" : 1, "P2" : 1, "P4" : 1, "Q3" : 1},
                  "P4" : {"O4" : 1, "P3" : 1, "Q4" : 1},
                  "P20" : {"O20" : 1, "Q20" : 1},
                  "P25" : {"P26" : 1, "Q25" : 1},
                  "P26" : {"O26" : 1, "P25" : 1, "P27" : 1, "Q26" : 1},
                  "P27" : {"O27" : 1, "P26" : 1, "Q27" : 1},
                  "P35" : {"O35" : 1, "P36" : 1, "Q35" : 1},
                  "P36" : {"O36" : 1, "P35" : 1, "P37" : 1, "Q36" : 1},
                  "P37" : {"O37" : 1, "P36" : 1, "P38" : 1, "Q37" : 1},
                  "P38" : {"O38" : 1, "P37" : 1, "P39" : 1, "Q38" : 1},
                  "P39" : {"O39" : 1, "P38" : 1, "P40" : 1, "Q39" : 1},
                  "P40" : {"O40" : 1, "P39" : 1, "Q40" : 1},
                  "Q1" : {"P1" : 1, "Q2" : 1, "R1" : 1},
                  "Q2" : {"P2" : 1, "Q1" : 1, "Q3" : 1, "R2" : 1},
                  "Q3" : {"P3" : 1, "Q2" : 1, "Q4" : 1, "R3" : 1},
                  "Q4" : {"P4" : 1, "Q3" : 1, "R4" : 1},
                  "Q20" : {"P20" : 1, "Q21" : 1, "R20" : 1},
                  "Q21" : {"Q20" : 1, "R21" : 1},
                  "Q24" : {"Q25" : 1, "R24" : 1},
                  "Q25" : {"P25" : 1, "Q24" : 1, "Q26" : 1, "R25" : 1},
                  "Q26" : {"P26" : 1, "Q25" : 1, "Q27" : 1, "R26" : 1},
                  "Q27" : {"P27" : 1, "Q26" : 1, "R27" : 1},
                  "Q35" : {"P35" : 1, "Q36" : 1, "R35" : 1},
                  "Q36" : {"P36" : 1, "Q35" : 1, "Q37" : 1, "R36" : 1},
                  "Q37" : {"P37" : 1, "Q36" : 1, "Q38" : 1, "R37" : 1},
                  "Q38" : {"P38" : 1, "Q37" : 1, "Q39" : 1, "R38" : 1},
                  "Q39" : {"P39" : 1, "Q38" : 1, "Q40" : 1, "R39" : 1},
                  "Q40" : {"P40" : 1, "Q39" : 1, "R40" : 1},
                  "R1" : {"Q1" : 1, "R2" : 1, "S1" : 1},
                  "R2" : {"Q2" : 1, "R1" : 1, "R3" : 1, "S2" : 1},
                  "R3" : {"Q3" : 1, "R2" : 1, "R4" : 1, "S3" : 1},
                  "R4" : {"Q4" : 1, "R3" : 1, "S4" : 1},
                  "R20" : {"Q20" : 1, "R21" : 1, "S20" : 1},
                  "R21" : {"Q21" : 1, "R20" : 1, "S21" : 1},
                  "R23" : {"R24" : 1, "S23" : 1},
                  "R24" : {"Q24" : 1, "R23" : 1, "R25" : 1, "S24" : 1},
                  "R25" : {"Q25" : 1, "R24" : 1, "R26" : 1, "S25" : 1},
                  "R26" : {"Q26" : 1, "R25" : 1, "R27" : 1, "S26" : 1},
                  "R27" : {"Q27" : 1, "R26" : 1, "R28" : 1, "S27" : 1},
                  "R28" : {"R27" : 1, "S28" : 1},
                  "R34" : {"R35" : 1, "S34" : 1},
                  "R35" : {"Q35" : 1, "R34" : 1, "R36" : 1, "S35" : 1},
                  "R36" : {"Q36" : 1, "R35" : 1, "R37" : 1, "S36" : 1},
                  "R37" : {"Q37" : 1, "R36" : 1, "R38" : 1, "S37" : 1},
                  "R38" : {"Q38" : 1, "R37" : 1, "R39" : 1, "S38" : 1},
                  "R39" : {"Q39" : 1, "R38" : 1, "R40" : 1, "S39" : 1},
                  "R40" : {"Q40" : 1, "R39" : 1, "S40" : 1},
                  "S1" : {"R1" : 1, "S2" : 1, "T1" : 1},
                  "S2" : {"R2" : 1, "S1" : 1, "S3" : 1, "T2" : 1},
                  "S3" : {"R3" : 1, "S2" : 1, "S4" : 1, "T3" : 1},
                  "S4" : {"R4" : 1, "S3" : 1, "T4" : 1},
                  "S20" : {"R20" : 1, "S21" : 1, "T20" : 1},
                  "S21" : {"R21" : 1, "S20" : 1, "S22" : 1, "T21" : 1},
                  "S22" : {"S21" : 1, "S23" : 1, "T22" : 1},
                  "S23" : {"R23" : 1, "S22" : 1, "S24" : 1, "T23" : 1},
                  "S24" : {"R23" : 1, "S23" : 1, "S25" : 1, "T24" : 1},
                  "S25" : {"R23" : 1, "S24" : 1, "S26" : 1, "T25" : 1},
                  "S26" : {"R23" : 1, "S25" : 1, "S27" : 1, "T26" : 1},
                  "S27" : {"R23" : 1, "S26" : 1, "S28" : 1, "T27" : 1},
                  "S28" : {"R23" : 1, "S27" : 1, "S29" : 1, "T28" : 1},
                  "S29" : {"S28" : 1, "S30" : 1, "T29" : 1},
                  "S30" : {"S29" : 1, "S31" : 1, "T30" : 1},
                  "S33" : {"S34" : 1, "T33" : 1},
                  "S34" : {"R34" : 1, "S33" : 1, "S35" : 1, "T34" : 1},
                  "S35" : {"R35" : 1, "S34" : 1, "S36" : 1, "T35" : 1},
                  "S36" : {"R36" : 1, "S35" : 1, "S37" : 1, "T36" : 1},
                  "S37" : {"R37" : 1, "S36" : 1, "S38" : 1, "T37" : 1},
                  "S38" : {"R38" : 1, "S37" : 1, "S39" : 1, "T38" : 1},
                  "S39" : {"R39" : 1, "S38" : 1, "S40" : 1, "T39" : 1},
                  "S40" : {"R40" : 1, "S39" : 1, "T40" : 1},
                  "T1" : {"S1" : 1, "T2" : 1},
                  "T2" : {"S2" : 1, "T1" : 1, "T3" : 1},
                  "T3" : {"S3" : 1, "T2" : 1, "T4" : 1},
                  "T4" : {"S4" : 1, "T3" : 1, "T5" : 1},
                  "T5" : {"T4" : 1, "T6" : 1},
                  "T6" : {"T5" : 1, "T7" : 1},
                  "T7" : {"T6" : 1, "T8" : 1},
                  "T8" : {"T7" : 1, "T9" : 1},
                  "T9" : {"T8" : 1, "T10" : 1},
                  "T10" : {"T9" : 1, "T11" : 1},
                  "T11" : {"T10" : 1, "T12" : 1},
                  "T12" : {"T11" : 1, "T13" : 1},
                  "T13" : {"T12" : 1, "T14" : 1},
                  "T14" : {"T13" : 1, "T15" : 1},
                  "T15" : {"T14" : 1, "T16" : 1},
                  "T16" : {"T15" : 1, "T17" : 1},
                  "T17" : {"T16" : 1, "T18" : 1},
                  "T18" : {"T17" : 1, "T19" : 1},
                  "T19" : {"T18" : 1, "T20" : 1},
                  "T20" : {"S20" : 1, "T19" : 1, "T21" : 1},
                  "T21" : {"S21" : 1, "T20" : 1, "T22" : 1},
                  "T22" : {"S22" : 1, "T21" : 1, "T23" : 1},
                  "T23" : {"S23" : 1, "T22" : 1, "T24" : 1},
                  "T24" : {"S24" : 1, "T23" : 1, "T25" : 1},
                  "T25" : {"S25" : 1, "T24" : 1, "T26" : 1},
                  "T26" : {"S26" : 1, "T25" : 1, "T27" : 1},
                  "T27" : {"S27" : 1, "T26" : 1, "T28" : 1},
                  "T28" : {"S28" : 1, "T27" : 1, "T29" : 1},
                  "T29" : {"S29" : 1, "T28" : 1, "T30" : 1},
                  "T30" : {"S30" : 1, "T29" : 1, "T31" : 1},
                  "T31" : {"T30" : 1, "T32" : 1},
                  "T32" : {"T31" : 1, "T33" : 1},
                  "T33" : {"S33" : 1, "T32" : 1, "T34" : 1},
                  "T34" : {"S34" : 1, "T33" : 1, "T35" : 1},
                  "T35" : {"S35" : 1, "T34" : 1, "T36" : 1},
                  "T36" : {"S36" : 1, "T35" : 1, "T37" : 1},
                  "T37" : {"S37" : 1, "T36" : 1, "T38" : 1},
                  "T38" : {"S38" : 1, "T37" : 1, "T39" : 1},
                  "T39" : {"S39" : 1, "T38" : 1, "T40" : 1},
                  "T40" : {"S40" : 1, "T39" : 1}
               }
   return graph_dict

# ------------------------------------------------------------------- Aimacode Repository Classes ------------------------------------------------------------------------
# Graph class taken from the aimacode repository
class Graph:
    """A graph connects nodes (vertices) by edges (links). Each edge can also
    have a length associated with it. The constructor call is something like:
        g = Graph({'A': {'B': 1, 'C': 2})
    this makes a graph with 3 nodes, A, B, and C, with an edge of length 1 from
    A to B,  and an edge of length 2 from A to C. You can also do:
        g = Graph({'A': {'B': 1, 'C': 2}, directed=False)
    This makes an undirected graph, so inverse links are also added. The graph
    stays undirected; if you add more links with g.connect('B', 'C', 3), then
    inverse link is also added. You can use g.nodes() to get a list of nodes,
    g.get('A') to get a dict of links out of A, and g.get('A', 'B') to get the
    length of the link from A to B. 'Lengths' can actually be any object at
    all, and nodes can be any hashable object."""

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """Make a digraph into an undirected graph by adding symmetric edges."""
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)

    def connect(self, A, B, distance=1):
        """Add a link from A and B of given distance, and also add the inverse
        link if the graph is undirected."""
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)

    def connect1(self, A, B, distance):
        """Add a link from A to B of given distance, in one direction only."""
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        """Return a link distance or a dict of {node: distance} entries.
        .get(a,b) returns the distance or None;
        .get(a) returns a dict of {node: distance} entries, possibly {}."""
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        """Return a list of nodes in the graph."""
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
     
# Graph Problem class to create the problem from a given graph and solve it
class GraphProblem(search.Problem):
    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph
        
   # Function that takes a vertex as input and returns a list of the vertices connected to it
    def actions(self, A):
        """The actions at a graph node are just its neighbors."""
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (self.graph.get(A, B) or search.np.inf)

    def find_min_edge(self):
        """Find minimum value of edges."""
        m = search.np.inf
        for d in self.graph.graph_dict.values():
            local_min = min(d.values())
            m = min(m, local_min)

        return m

   # Heuristic function using the straight-line distance
    def h(self, node):
        """h function is straight-line distance from a node's state to goal."""
        locs = getattr(self.graph, 'locations', None)
        if locs:
            if type(node) is str:
                return int(search.distance(locs[node], locs[self.goal]))

            return int(search.distance(locs[node.state], locs[self.goal]))
        else:
            return search.np.inf

# Breadth first search method from the Aimacode repository, modified to calculate the amount of steps found from the initial to the goal and the total number of visited vertices
# Returns the Goal node, the amount of steps from the taken path, and the number of vertices visited in total
def breadth_first_graph_search(problem):
    """[Figure 3.11]
    Note that this function can be implemented in a
    single line as below:
    return graph_search(problem, FIFOQueue())
    """
    node = search.Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = search.deque([(node, 0)])
    explored = set()
    while frontier:
        q_pop = frontier.popleft()
        node = q_pop[0]
        if node.state in explored:
           continue
        explored.add(node.state)
      #   print("Now in Node:", q_pop)
        for child in node.expand(problem):
            if child.state not in explored:
                if problem.goal_test(child.state):
                    return (child, q_pop[1] + 1), len(explored)
                frontier.append((child, q_pop[1] + 1))
    return None

# Depth first search method from the Aimacode repository, modified to calculate the amount of steps found from the initial to the goal and the total number of visited vertices
# Returns the Goal node, the amount of steps from the taken path, and the number of vertices visited in total
def depth_first_graph_search(problem):
    """
    [Figure 3.7]
    Search the deepest nodes in the search tree first.
    Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Does not get trapped by loops.
    If two paths reach a state, only use the first one.
    """
    frontier = [((search.Node(problem.initial)), 0)]  # Stack

    explored = set()
    while frontier:
        s_pop = frontier.pop()
        node = s_pop[0]
        if node.state in explored:
           continue
      #   print(s_pop)
        if problem.goal_test(node.state):
            return s_pop, len(explored)
        explored.add(node.state)
        frontier.extend((child, s_pop[1] + 1) for child in node.expand(problem)
                        if child.state not in explored)
    return None

# Best first search method from the Aimacode repository
# Returns the goal node if found and the number of total visited vertices
def best_first_graph_search(problem, f, display=False):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = search.memoize(f, 'f')
    node = search.Node(problem.initial)
    frontier = search.PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
            return node, len(explored)
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None

# Uniform cost search method from the Aimacode repository
def uniform_cost_search(problem, display=False):
    """[Figure 3.14]"""
    return best_first_graph_search(problem, lambda node: node.path_cost, display)

# Creating graph and problem objects 
graph = search.Graph(get_graph_dict())
problem_3_9 = search.GraphProblem("R3", "B38", graph)

# Using Breadth first search, Depth first search and Uniform cost search to reach the goal
bfs = breadth_first_graph_search(problem_3_9)
dfs = depth_first_graph_search(problem_3_9)
ucs = uniform_cost_search(problem_3_9)

# Printing results from a Breadth first search, Depth first search and Uniform cost search
print("\nBreadth First Search:\nGoal: " + str(bfs[0][0]) + "\nVertices in Path: " + str(bfs[0][1]) + "\nTotal Visited Vertices: " + str(bfs[1]))
print("\nDepth First Search:\nGoal: " + str(dfs[0][0]) + "\nVertices in Path: " + str(dfs[0][1]) + "\nTotal Visited Vertices: " + str(dfs[1]))
print("\nUniform Cost Search:\nGoal: " + str(ucs[0]) + "\nTotal Visited Vertices: " + str(ucs[1]))