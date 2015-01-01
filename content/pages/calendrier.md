Title: Calendrier


<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>
<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
<script src="//momentjs.com/downloads/moment-with-locales.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.2.5/fullcalendar.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.2.5/lang/fr.js"></script>
<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.2.5/fullcalendar.min.css"></link>
<link media="print" href="//cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.2.5/fullcalendar.print.css"></link>

<div id='calendar'></div>
<style>

.entry-title {
  display: none;
}

#calendar {
  max-width: 900px;
  margin: 0px auto;
  padding-bottom: 25px;
  padding-left: 10px;
  padding-right: 10px;
}

.fc-toolbar h2 {
  text-transform: capitalize;
}

body .fc {
  max-width: 900px !important;
  font-size: 11pt;
}


</style>

<script>
$(document).ready(function() {
    moment().format("Do MMM YY");
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek'
        },
        defaultView: "month",
        eventLimit: true,
        events: [
          {
            title: 'Trail du Vieux Semur',
            start: '2015-01-17',
            url: 'http://www.trailduvieuxsemur.com'
          },
          {
            title: 'Transvaal Trail',
            start: '2015-02-14',
            url: 'http://www.stjodijon.com/transvaal-trail.html'
          },
          {
            title: 'Semi de Nuits',
            start: '2015-03-14',
            url: 'http://www.semi-nuits-st-georges.com'
          },
          {
            title: '10k de Chalons',
            start: '2015-03-29',
            url: 'http://www.10kmdechalonsursaone.fr'
          },
          {
            title: "10KM au fil de l'eau",
            start: '2015-05-02',
            url: 'http://asvbdjogging.fr'
          },
          {
            title: 'Marathon de Berlin',
            start: '2015-09-27',
            url: 'http://www.bmw-berlin-marathon.com'
          },

        ]

    });
});

</script>
