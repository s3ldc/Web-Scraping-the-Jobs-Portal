from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    # Find all the text that is present in h5 tag
    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text)

    # Display the course name and its price
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')