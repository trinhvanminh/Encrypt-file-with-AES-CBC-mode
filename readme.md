
# AES CBC mode

**Command line**:

	python 1712601.py -i <filename> -k <key> -m <mode: e/d>

or

    python 1712601_raw.py -i <filename> -k <key> -m <mode: e/d>


For example:
```
python 1712601.py -i a.txt -k 11111111 -m e

```
> verify OTP code

And the result was a encrypted file

> return a.txt.enc

	python 1712601.py -i a.txt.enc -k 11111111 -m d
   
> verify OTP code
    
The plantext file:
> return a.txt


**Note**

* OTP code will change after 30s

* allowed wrong OTP number is 2


**Not complete:**

	vi. 	Chương trình có tính năng phát hiện các dấu hiệu bất thường 
    		và xử lý phù hợp (ví dụ: thấy nội dung không như ban đầu
    		(bị crack hoặc có virus bám vào) thì tự khôi phục lại, 
    		thấy môi trường chạy không phải là môi trường "lành mạnh" 
    		(bị chạy trong sandbox hoặc trong chế độ debug, 
    		chương trình không nằm trong đĩa /máy được quy ước, ...)
    		thì không chạy /tự hủy /gây lỗi hệ thống, ...)

**Goal:**

Xây dựng chương trình mã hóa & giải mã một tâp tin thỏa:

i.  Key mã hóa (password) do người dùng nhập vào 
    được hash thành 1 chuỗi tối thiểu 100bit.

ii. Chương trình có thể nhận tham số dòng lệnh - 
    không có hoặc tham số sai thì mới yêu cầu người dùng 
    chỉ định tên file mã hóa /giải mã 

iii. Tuy cùng 1 key mã hóa nhưng mỗi lần mã sẽ 
    phải được một kết quả khác nhau 
    (về cả chiều dài lẫn nội dung nhị phân).

iv. Chương trình mã hóa có obfuscasted code để tăng độ an toàn, 
    tránh không cho người khác dò ra cách làm và giải mã.

v.  Mỗi khi chương trình chạy phải hỏi 
    và kiểm tra 1 mật khẩu "động" 
    và nếu đúng thì mới tiếp tục chạy.

vi. Chương trình có tính năng phát hiện các dấu hiệu bất thường 
    và xử lý phù hợp (ví dụ: thấy nội dung không như ban đầu
    (bị crack hoặc có virus bám vào) thì tự khôi phục lại, 
    thấy môi trường chạy không phải là môi trường "lành mạnh" 
    (bị chạy trong sandbox hoặc trong chế độ debug, 
    chương trình không nằm trong đĩa /máy được quy ước, ...)
    thì không chạy /tự hủy /gây lỗi hệ thống, ...)



