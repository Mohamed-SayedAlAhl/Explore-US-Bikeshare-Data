import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #  getting user input for city (chicago, new york city, washington). 
    while True:
        city=input("Enter the city you would like to see its data from (chicago , new york city or washington) : ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Wrong city name")

    #  getting user input for month (all, january, february, ... , june)
    while True:
        month=input("Enter month name to filter the data upon or simply enter all for no filter: ").lower()
        months=['january','february','march','april','may','june','july','august','September','october','november','december']
        if month in months or month=='all':
            break
        else:
            print("Wrong month name")



    #  getting user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Enter day name to filter the data upon or simply enter all for no filter: ").lower()
        days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        if day in days or day=='all':
            break
        else:
            print("Wrong day name")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name
    if month!='all':
        months=['january','february','march','april','may','june','july','august','September','october','november','december']
        month=months.index(month)+1
        df=df[df['month']==month]
    if day!='all':
        df=df[df['day']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displaying the most common month
    popular_month=df['month'].mode()[0]
    print(f"most common month  is {popular_month} ")
    # displaying the most common day of week

    popular_day=df['day'].mode()[0]
    print(f"most common day of week is {popular_day} ")
    #displaying the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print(f"most common start hour is {popular_hour} ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # displaying most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print(f"most commonly used start station is {popular_start_station}")


    #displaying most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print(f"most commonly used end station is {popular_end_station}")

    # displaying most frequent combination of start station and end station trip
    df['start_end_station']=df['Start Station']+" "+df['End Station']
    popular_start_end=df['start_end_station'].mode()[0]
    print(f"most frequent start and end station combination is {popular_start_end}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:',earliest_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   
def raw_data(df):
    """Displays raw data on reaquest of the user."""
    while(True):
         view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
         if view_data=='yes' or view_data=='no':
            break
         else:
            print("please enter yes or no only: ")
    start_loc = 0
    while (view_data=='yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display=='yes':
            continue
        elif view_display=='no':
            break
        else:
            while(True):
                print("please enter yes or no only: ")
                re_view_display = input("Do you wish to continue?: ").lower()
                if re_view_display =='yes' or re_view_display =='no':
                    break
            if re_view_display=='yes':
                continue
            elif re_view_display=='no':
                break 
            
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
