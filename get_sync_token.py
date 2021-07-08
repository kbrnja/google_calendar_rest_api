
from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',          #calendar only
          'https://www.googleapis.com/auth/calendar.events.readonly']   #events

kwargs = ("sync_token", '123')

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token_sync.json'):
        creds = Credentials.from_authorized_user_file('token_sync.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES, **kwargs)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token_sync.json', 'w') as token:
            token.write(creds.to_json())

    if InstalledAppFlow.from_client_secrets_file( 'credentials.json', SCOPES, **kwargs) = None
    print('Performing full sync.')

##    // Set the filters you want to use during the full sync.Sync tokens aren't compatible with
#    // most filters, but you may want to limit your full sync to only a certain date range.
#    // In this example we are only syncing events up to a year old.
#    Date oneYearAgo = Utils.getRelativeDate(java.util.Calendar.YEAR, -1);
#    request.setTimeMin(new DateTime(oneYearAgo, TimeZone.getTimeZone("UTC")));
    else:
        print('Performing incremental sync.')
    request.setSyncToken(syncToken)



    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Refresh the token')

if __name__ == '__main__':
    main()