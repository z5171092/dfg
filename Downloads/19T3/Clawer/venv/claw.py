# -*- coding: utf-8 -*-
import requests, re, json
import csv


def getHouseNumber(url):
    html = requests.get(url)
    data = html.text
    # regularization
    urlbase = re.search('"remarketing_ids":\[(.*?)\],', data)

    url = []
    urlNumber = ''
    for e in urlbase.group(1):
        if e == ",":
            url.append(urlNumber)
            urlNumber = ''
        else:
            urlNumber = urlNumber + e

    return url


def getHouseInformation(urlNumber):
    Url = 'https://zh.airbnb.com/api/v2/pdp_listing_details/' + str(
        urlNumber) + '?_format=for_rooms_show&adults=1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&'
    html = requests.get(Url)
    data = json.loads(html.text)
    House_owner = data['pdp_listing_detail']['user'].get('host_name')
    price_url = 'https://zh.airbnb.com/api/v2/pdp_listing_booking_details?force_boost_unc_priority_message_type=&guests=1&listing_id=' + str(
        urlNumber) + '&show_smart_promotion=0&_format=for_web_dateless&_interaction_type=pageload&_intents=p3_book_it&_parent_request_uuid=4527592d-6c3c-4b64-9c40-b814fb4ca733&_p3_impression_id=p3_1547785606_MzQbhXiFnlGGppGx&number_of_adults=1&number_of_children=0&number_of_infants=0&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=zh'
    price_html = requests.get(price_url)
    price_data = json.loads(price_html.text)
    price = price_data['pdp_listing_booking_details'][0]['rate_with_service_fee'].get('amount_formatted')
    Introduction_housing = data['pdp_listing_detail']['sectioned_description'].get('description')
    Position = data['pdp_listing_detail'].get('location_title')

    HouseName = data['pdp_listing_detail'].get('name')

    Information = []
    Information.append(HouseName)
    Information.append(House_owner)
    Information.append(price)
    Information.append(Introduction_housing)
    Information.append(Position)

    return Information


def main(i):
    HouseNumberUrl = "https://zh.airbnb.com/api/v2/explore_tabs?version=1.4.5&satori_version=1.1.3&_format=for_explore_search_web&experiences_per_grid=20&items_per_grid=18&guidebooks_per_grid=20&auto_ib=false&fetch_filters=true&has_zero_guest_treatment=true&is_guided_search=true&is_new_cards_experiment=true&luxury_pre_launch=true&query_understanding_enabled=false&show_groupings=true&supports_for_you_v3=true&timezone_offset=480&client_session_id=53638ce3-becb-444f-bfdd-d6b301b93456&metadata_only=false&is_standard_search=true&refinement_paths%5B%5D=%2Fhomes&selected_tab_id=home_tab&adults=0&children=0&infants=0&toddlers=0&place_id=ChIJkVLh0Aj0AzQRyYCStw1V7v0&allow_override%5B%5D=&s_tag=BoUbRf3d&section_offset=6&items_offset=" + str(
        7 * i) + "&screen_size=medium&query=%E6%B7%B1%E5%9C%B3&_intents=p1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=zh"
    out = open('Details.csv', 'a', newline='', encoding='utf-8-sig')
    csv_write = csv.writer(out, dialect='excel')
    for number in getHouseNumber(HouseNumberUrl):
        stu2 = getHouseInformation(number)
        csv_write.writerow(stu2)
        print("write over")


if __name__ == '__main__':

    stu1 = ['HouseName', 'House_owner', 'price', 'Introduction_housing', 'Position']
    out = open('Stu_csv.csv', 'a', newline='', encoding='utf-8-sig')
    csv_write = csv.writer(out, dialect='excel')
    csv_write.writerow(stu1)
    #Here is the page number, u can change it
    for i in range(1):
        main(i)
