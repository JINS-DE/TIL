from datetime import datetime, timedelta

def get_review_dates():
    """
    오늘 날짜를 기준으로 1-4-7-30 복습법에 따른 복습 날짜를 계산한다
    """
    today = datetime.now()
    review_intervals = [1, 4, 7, 30]
    review_dates={}

    for days in review_intervals:
        review_date = today - timedelta(days=days)
        review_dates[f'{days}일 전'] = review_date.strftime('%Y년 %m월 %d일')
    
    return review_dates

if __name__ ==  "__main__":
    dates_to_review = get_review_dates()
    print("📖 오늘 복습할 TIL 날짜입니다.\n")
    for interval, date_str in dates_to_review.items():
        print(f"- {interval} ({date_str} 기록)")    