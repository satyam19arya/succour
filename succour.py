import webbrowser

if __name__ == "__main__":

    calamities=['S','E','W','C','L','D']
    print("\nHi there, Welcome to Succour!\nHow can we help you?\n")
    cal=input("Press:\nS for our official website\nE for Earthquake related queries\nW for Windslides related queries\nC for Cyclone related queries\nL for Landslide related queries\nD for Donation\n->")
    if cal==calamities[0]:
        webbrowser.open('https://my-aws-bucket-for-hackathon.s3.ap-south-1.amazonaws.com/natural_disaster/index.html')
    elif cal==calamities[1]:
        webbrowser.open('https://my-aws-bucket-for-hackathon.s3.ap-south-1.amazonaws.com/natural_disaster/Newfolder/Earthquake.html')
    elif cal==calamities[2]:
        webbrowser.open('https://my-aws-bucket-for-hackathon.s3.ap-south-1.amazonaws.com/natural_disaster/Newfolder/Wing_storm.html')
    elif cal==calamities[3]:
        webbrowser.open('https://my-aws-bucket-for-hackathon.s3.ap-south-1.amazonaws.com/natural_disaster/Newfolder/Cyclone.html')
    elif cal==calamities[4]:
        webbrowser.open('https://my-aws-bucket-for-hackathon.s3.ap-south-1.amazonaws.com/natural_disaster/Newfolder/Landslide.html')
    elif cal==calamities[5]:
        webbrowser.open('https://my-aws-bucket-for-hackathon.s3.ap-south-1.amazonaws.com/natural_disaster/Newfolder/form/index.html')