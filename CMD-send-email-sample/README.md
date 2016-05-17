# Sample sending email using gmail service

### Usage

    git clone https://github.com/0x8BADFOOD/python-experiments.git
    cd python-experiments/CMD-send-email-sample
    chmod +x send_mail.py

### Change following values:

    recepients_list =[
        "your_mail1@gmail.com"
        "your_mail2@gmail.com",
    ]
    EMAIL_FROM        = "USER.NAME@gmail.com"
    EMAIL_LOGIN       = "USER.NAME"
    EMAIL_PASSWORD    = "WW91ciBwYXNzd29yZA=="

**PASSWORD in 64 base** so you need prepare you password in base64:

    #!/usr/bin/python
    import base64
    base64_password = base64.b64encode("Your password")
    print base64_password 
    #Ouput: WW91ciBwYXNzd29yZA==

### Run script:

    ./send_mai.py
