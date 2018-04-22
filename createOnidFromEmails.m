clear;
close all;

fid_read = fopen('CS362_S18_emails.txt','r');
fid_write = fopen('CS362_S18_onids.txt','a');

line = fgetl(fid_read);
stripped_string = split(line,'@');
fprintf(fid_write,sprintf('%s\n',stripped_string{1}));

while ischar(line)
    line = fgetl(fid_read);
    stripped_string = split(line,'@');
    fprintf(fid_write,sprintf('%s,\n',stripped_string{1}));
end

fclose('all');