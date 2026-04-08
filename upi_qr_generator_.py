import qrcode

#taking input upi
upi_id = input("enter your UPI ID = ")

#upi://paY?pa=UPI_ID&apn=NAME&am=Amoount&cu=CURRENCY&tn=MESSAGE
#PN,AM,CU ,tn=PARAMETERS
#PA=UP ID,Pn=recipient name,am=amount,cu=currency,tn=payment message,mc is merchant code

#defining the ppayment url besd on upi id and payment app
# f string jo ki string format keliya hota variable ko string mai mbit kiya hai
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr code for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the qr code to image file

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#pil viewer=image processing (to display qr code)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
