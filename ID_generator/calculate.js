/*LATVIAN IDDDDDDDDDDDDDDD*/

var currentDate = new Date();

$("#LV").click(() =>{ 

 $("#result").text(getRandomPersonalId);
 $("#phone").text(generate_random_phone_and_email_LV(25500001,25599999,"+371")[0]);
 $("#email").text(generate_random_phone_and_email_LV(25500001,25599999,"+371")[1]);
 $("#document").text(generate_document_number_LV(1000000,9999999));
 $('#iban').text("LV41HABA0551003550352");

});


function getRandomPersonalId() {
  var currentDate = new Date();

  var maxAgeInMilis = 45 * 365 * 24 * 60 * 60 * 1000;
  var minAgeInMilis = 21 * 365 * 24 * 60 * 60 * 1000;
  var randomMilis = Math.floor((Math.random() * maxAgeInMilis) + minAgeInMilis);

  var time = currentDate.setTime(currentDate.getTime() - randomMilis);
  var date = new Date(time);

  var day = padWithLeadingZeros(date.getDate());
  var month = padWithLeadingZeros(date.getMonth() + 1);
  var shortYear = date.getFullYear().toString().substring(2);
  var firstPart = day + "" + month + "" + shortYear;

  var checkDigit = "00";
  while (checkDigit.toString().length == 2) {
    pk = firstPart + getSecondPart();
    checkDigit = getCheckDigit(pk);
  };

  pk = pk + checkDigit;
  pk = pk.substring(0, 6) + "-" + pk.substring(6);

  return pk;
};

function padWithLeadingZeros(value) {
  value = value.toString();
  return value.length == 1 ? "0".concat(value) : value;
};

function getCheckDigit(pk) {
  var factor = [1, 6, 3, 7, 9, 10, 5, 8, 4, 2];

  pk = pk.split("").map(i => parseInt(i));

  var reduce = pk.reduce((prev, cur, i) => cur * factor[i] + prev);

  return (1101 - reduce) % 11;
};

function getSecondPart() {
  return "1" + Math.floor((Math.random() * 899) + 100);
};


/*ESTONIAN IDDDDDDDDDDDDDDD*/

function generateEstonianPersonalID()
{
  gender=randomIntFromInterval(3,4);
  year=randomIntFromInterval(60,94).toString();
  month=pad(randomIntFromInterval(1,12).toString(),2);
  day=pad(randomIntFromInterval(1,28).toString(),2);
  rndpart=pad(randomIntFromInterval(1,999).toString(),3);
  var digits = (gender+year+month+day+rndpart).split("");
  var scale1sum = (1*parseInt(digits[0]) + 2*parseInt(digits[1]) + 3*parseInt(digits[2]) + 4*parseInt(digits[3]) + 5*parseInt(digits[4]) + 6*parseInt(digits[5]) + 7*parseInt(digits[6]) + 8*parseInt(digits[7]) + 9*parseInt(digits[8]) + 1*parseInt(digits[9]));
  var checksum = scale1sum%11;
  if(checksum===10)  {
      var scale2sum = (3*parseInt(digits[0]) + 4*parseInt(digits[1]) + 5*parseInt(digits[2]) + 6*parseInt(digits[3]) + 7*parseInt(digits[4]) + 8*parseInt(digits[5]) + 9*parseInt(digits[6]) + 1*parseInt(digits[7]) + 2*parseInt(digits[8]) + 3*parseInt(digits[9]));
      checksum = scale2sum%11;
      if(checksum===10) checksum = 0;
  }
  personalID=gender+year+month+day+rndpart+checksum;
  return personalID;
}
function randomIntFromInterval(min,max)
{
    return Math.floor(Math.random()*(max-min+1)+min);
}
function pad(n, width, z) {
  z = z || '0';
  n = n + '';
  return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}


$("#EE").click(() =>{ 

 $("#result").text(generateEstonianPersonalID);
 $("#phone").text(generate_random_phone_and_email_EE(500000011,509999999,"+372")[0]);
 $("#email").text(generate_random_phone_and_email_EE(500000011,509999999,"+372")[1]);
 $("#document").text(generate_document_number_EE(1000000,9999999));
 $('#iban').text("EE501277518211896395");


});

$("#LT").click(() =>{ 

 $("#result").text(generateEstonianPersonalID);
 $("#phone").text(generate_random_phone_and_email_LT(65500001,65599999,"+370")[0]);
 $("#email").text(generate_random_phone_and_email_LT(65500001,65599999,"+370")[1]);
 $("#document").text(generate_document_number_EE(1000000,9999999));
 $('#iban').text("LT482993375427946621");

});

/*POLISH IDDDDDDDDDDDDDDD*/


function generatePesel()
{
  year=randomIntFromInterval(60,94).toString();
  month=pad(randomIntFromInterval(1,12).toString(),2);
  day=pad(randomIntFromInterval(1,28).toString(),2);
  rndpart=pad(randomIntFromInterval(1,9999).toString(),4);
  var digits = (""+year+month+day+rndpart).split("");
  var checksum = (1*parseInt(digits[0]) + 3*parseInt(digits[1]) + 7*parseInt(digits[2]) + 9*parseInt(digits[3]) + 1*parseInt(digits[4]) + 3*parseInt(digits[5]) + 7*parseInt(digits[6]) + 9*parseInt(digits[7]) + 1*parseInt(digits[8]) + 3*parseInt(digits[9]))%10;
  if(checksum==0) checksum = 10;
  checksum = 10 - checksum;
  pesel=year+month+day+rndpart+checksum;
  return pesel;
}
 
function randomIntFromInterval(min,max){
    return Math.floor(Math.random()*(max-min+1)+min);
}
function pad(n, width, z) {
  z = z || '0';
  n = n + '';
  return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}


$("#PL").click(() =>{ 

 $("#result").text(generatePesel);
 $("#phone").text(generate_random_phone_and_email_PL(785000001,785999999,"+48")[0]);
 $("#email").text(generate_random_phone_and_email_PL(785000001,785999999,"+48")[1]);
 $("#document").text(generate_document_number_PL(100000,999999));
 $('#iban').text("PL05109024022449341799116585");

});


function generate_random_phone_and_email_EE(min,max,index)
{
    rnd_number = randomIntFromInterval(50000011,50999999);
    return [index+rnd_number,'api_ee_test_'+rnd_number+'@inbank.ee'];
}


function generate_random_phone_and_email_LV(min,max,index)
{
    rnd_number = randomIntFromInterval(25500001,25599999);
    return [index+rnd_number,'api_ee_test_'+rnd_number+'@inbank.ee'];
}



function generate_random_phone_and_email_LT(min,max,index)
{
    rnd_number = randomIntFromInterval(65500001,65599999);
    return [index+rnd_number,'api_ee_test_'+rnd_number+'@inbank.ee'];
}



function generate_random_phone_and_email_PL(min,max,index)
{
    rnd_number = randomIntFromInterval(785000001,785999999);
    return [index+rnd_number,'api_ee_test_'+rnd_number+'@inbank.ee'];
}


function generate_document_number_EE(min,max)
{
    rnd_number = randomIntFromInterval(1000000,9999999);
    return  'PS'+rnd_number;
}

function generate_document_number_LV(min,max)
{
    rnd_number = randomIntFromInterval(1000000,9999999);
    return  'PA'+rnd_number;
}

function generate_document_number_PL(min,max)
{
    rnd_number = randomIntFromInterval(400000,499999);
    return  'ACI'+rnd_number;
}

// var data
/*For modifying gender, birth date, etc*/
// $("form").on("submit", function() {
  // store the value of the input with name='age' 
  //  var age = $(this).find('[name=age]').val();

  // console.log($('form').serializeArray());
// });


$('#submit').click((event)=>{
  event.preventDefault();
  let formdata = ($('form').serializeArray());
  let formBithday = formdata[0].value;
  let formGender = formdata[1].value;
  let country = formdata[2].value;

  if (country=="EE"){
    if (formGender=='male') {gender = 3;}
    else {gender=4}
    
    year=formBithday.slice(0,4);
    month=formBithday.slice(5,7);
    day=formBithday.slice(8,10);
    rndpart=pad(randomIntFromInterval(1,999).toString(),3);
    var digits = (gender+year+month+day+rndpart).split("");
    var scale1sum = (1*parseInt(digits[0]) + 2*parseInt(digits[1]) + 3*parseInt(digits[2]) + 4*parseInt(digits[3]) + 5*parseInt(digits[4]) + 6*parseInt(digits[5]) + 7*parseInt(digits[6]) + 8*parseInt(digits[7]) + 9*parseInt(digits[8]) + 1*parseInt(digits[9]));
    var checksum = scale1sum%11;
    if(checksum===10)  {
        var scale2sum = (3*parseInt(digits[0]) + 4*parseInt(digits[1]) + 5*parseInt(digits[2]) + 6*parseInt(digits[3]) + 7*parseInt(digits[4]) + 8*parseInt(digits[5]) + 9*parseInt(digits[6]) + 1*parseInt(digits[7]) + 2*parseInt(digits[8]) + 3*parseInt(digits[9]));
        checksum = scale2sum%11;
        if(checksum===10) checksum = 0;
    }
    personalID=gender+year+month+day+rndpart+checksum;
    $("#result").text(personalID);
    $("#phone").text(generate_random_phone_and_email_EE(500000011,509999999,"+372")[0]);
    $("#email").text(generate_random_phone_and_email_EE(500000011,509999999,"+372")[1]);
    $("#document").text(generate_document_number_EE(1000000,9999999));
  }
  else if(country=="PL"){
    year=formBithday.slice(0,4);
    month=formBithday.slice(5,7);
    day=formBithday.slice(8,10);
    rndpart=pad(randomIntFromInterval(1,9999).toString(),4);
    var digits = (""+year+month+day+rndpart).split("");
    var checksum = (1*parseInt(digits[0]) + 3*parseInt(digits[1]) + 7*parseInt(digits[2]) + 9*parseInt(digits[3]) + 1*parseInt(digits[4]) + 3*parseInt(digits[5]) + 7*parseInt(digits[6]) + 9*parseInt(digits[7]) + 1*parseInt(digits[8]) + 3*parseInt(digits[9]))%10;
    if(checksum==0) checksum = 10;
    checksum = 10 - checksum;
    pesel=year+month+day+rndpart+checksum;
    $("#result").text(pesel);
    $("#phone").text(generate_random_phone_and_email_PL(785000001,785999999,"+48")[0]);
    $("#email").text(generate_random_phone_and_email_PL(785000001,785999999,"+48")[1]);
    $("#document").text(generate_document_number_PL(100000,999999));   
  }
  
})


// console.log(data)
