input = int(input())            #inputに任意の値を入力できるようにする

q  = divmod(input,16)           # 変数input の数を16で割った商と余りを計算  戻り値 q[商,あまり]

sum = str(q[1])                 #"http://7ujm.net/play/DECtoHEX/TOH.html"(10進数⇔16進数)を参照。 変数input を16で割った余りを 変数sum に代入。


while q[0] > 0 :                #上のリンクより、商が0になるまでは①の処理を繰り返す

   q = divmod(q[0],16)#①        #変数inputの値を16で割ったその商を16で割って、その商を・・・　と続いていく

   if q[1] == 10:               #10進数での"10"は,16進数での"A"になる。同様に11はB,12はCといった感じ。
       j = "A"

   elif q[1] == 11:
        j = "B"

   elif q[1] == 12:
        j = "C"

   elif q[1] == 13:
        j = "D"

   elif q[1] == 14:
        j = "E"

   elif q[1] == 15:
        j = "F"

   else :
       j = str(q[1])            #10未満の数をまとめて処理。10未満の数字は16進数にしても変わらない。
       
   sum = j + sum                #       ・・・   　<2回目の①計算の余り> +  <1回目の①計算の余り> + <inputを16で割った余り>
                                #     <四桁目以降>      <三桁目>              <二桁目>              <一桁目>            #左のように今まで計算した結果を連結させて16進数をつくる。
   
   


print(sum) #出力して終了
