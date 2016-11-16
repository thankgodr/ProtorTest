def calculate_tax(dictArg):
  for i,v in dictArg.items():
    if dictArg[i] <= 1000:
      dictArg[i] = 0
    elif dictArg[i] <= 10000:
      dictArg[i] = (dictArg[i] - 1000) * 0.1
    elif dictArg[i] <= 20200:
      dictArg[i] = (dictArg[i]-10000) * 0.15 + 900
    elif dictArg[i] <= 30750:
      dictArg[i] = (dictArg[i]-20200) * 0.2 + 2430
    elif dictArg[i]  <= 50000:
      dictArg[i] = (dictArg[i] - 30730) * 0.25 + 4540
    else:
      dictArg[i] = (dictArg[i]-50000) * 0.3 + 9352.5
  return dictArg